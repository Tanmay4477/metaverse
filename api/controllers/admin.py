from sqlmodel import Session, select
from utils.wraper import ResponseWraper, ElementSchema, MapSchema, UpdateElementSchema, CreateAvatar
from utils.status_code import Http, Message
from models import Element, Space, SpaceElement, Avatar
from utils.auth import auth_wrapper
from fastapi import Depends, HTTPException

def create_element_controller(element: ElementSchema, db: Session, payload) -> ResponseWraper:
    try:
        if not payload['role'] == 'admin':
            raise HTTPException(status_code=403, detail="Admin not authenticated")

        exist_element = select(Element).where(Element.name == element.name)
        is_exist_element = db.exec(exist_element).first()
        if is_exist_element:
            raise HTTPException(status_code=400, detail="Please change the element name")
        db_element = Element.model_validate(element)
        db.add(db_element)
        db.commit()
        db.refresh(db_element)
        return ResponseWraper(status=Http.StatusOk, message=Message.CREATED, data=db_element.id)
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        raise HTTPException(status_code=500, detail="Catch Error found")

def update_element_controller(elementId: int, element: UpdateElementSchema, db: Session, payload) -> ResponseWraper:
    try:
        if not payload['role'] == 'admin':
            raise HTTPException(status_code=403, detail="Admin not authenticated")
        data = db.get(Element, elementId)
        if not data:
            raise HTTPException(status_code=400, detail="Element not present")
        element_data = element.model_dump(exclude_unset=True)
        data.sqlmodel_update(element_data)
        db.add(data)
        db.commit()
        db.refresh(data)
        return ResponseWraper(status=Http.StatusOk, message=Message.UPDATED, data=data.image_url)
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        raise HTTPException(status_code=500, detail="Catch Error found")

def create_map_controller(map: MapSchema, db: Session, payload) -> ResponseWraper:
    try:
        print("Start")
        if not payload['role'] == 'admin':
            raise HTTPException(status_code=403, detail="Admin not authenticated")
        exist_element = select(Space).where(Space.name == map.name)
        is_exist_element = db.exec(exist_element).first()
        if is_exist_element:
            raise HTTPException(status_code=400, detail="Please change the element name")
        
        db_element = Space(name=map.name, width=map.width, height=map.height, thumbnail=map.thumbnail, user_id=payload['id'])
        db.add(db_element)
        db.flush()
        for i in map.defaultElements:
            if i.x > db_element.width or i.y > db_element.height:
                raise HTTPException(status_code=400, detail="Not valid place of element")
            space_element = SpaceElement(x=i.x, y=i.y, element_id=i.id, space_id=db_element.id)
            db.add(space_element)
        db.commit()
        db.refresh(db_element)
        return ResponseWraper(status=Http.StatusOk, message=Message.CREATED, data=db_element.id)
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        raise HTTPException(status_code=500, detail="Catch Error found")


def create_avatar_controller(avatar: CreateAvatar, db: Session, payload) -> ResponseWraper:
    try:
        if not payload['role'] == 'admin':
            raise HTTPException(status_code=403, detail="Admin not authenticated")

        exist_element = select(Avatar).where(Avatar.name == avatar.name)
        is_exist_element = db.exec(exist_element).first()

        if is_exist_element:
            raise HTTPException(status_code=400, detail="Please change the element name")
        db_element = Avatar.model_validate(avatar)

        db.add(db_element)
        db.commit()
        db.refresh(db_element)
        return ResponseWraper(status=Http.StatusOk, message=Message.CREATED, data=db_element.id)
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        raise HTTPException(status_code=500, detail="Catch Error found")