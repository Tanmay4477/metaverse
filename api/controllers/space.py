from sqlmodel import Session, select
from utils.wraper import ResponseWraper, SpaceSchema, PayloadSchema, PostSpaceSchema, SpaceListWraper, GetSpaceWraper, AddElementSchema
from utils.status_code import Http, Message
from models import User, Space, SpaceElement
from utils.auth import auth_wrapper, get_password_hash, verify_password, encode_token, decode_token
from fastapi import HTTPException


def create_space_controller(space: SpaceSchema, db: Session, payload: PayloadSchema) -> ResponseWraper:
    try:
        if space.mapId:
            map = db.get(Space, space.mapId)
            print("My Map", map)
            if(map is None or map.user_detail.role != 'admin'):
                raise HTTPException(status_code=404, detail="Not Valid Map")

            statement = select(SpaceElement).where(SpaceElement.space_id == map.id)
            result = db.exec(statement).all()
            print("resu", result)
            print("OLD SPACE ELEMENT")
            space_data = Space(name=space.name, width=space.width or map.width, height=space.width or map.width, thumbnail=map.thumbnail, user_id=payload['id'])
            db.add(space_data)
            db.flush()
            for i in result:
                new_space_element = SpaceElement(element_id=i.element_id, x=i.x, y=i.y, space_id=space_data.id)
                db.add(new_space_element)
            db.commit()
            db.refresh(space_data)
            #  Do something
        else:
            space_data = Space(name=space.name, width=space.width, height=space.height, user_id=payload['id'])
            db.add(space_data)
            db.commit()
            db.refresh(space_data)
        print(space_data, "Space Data")
        return PostSpaceSchema(status=Http.StatusOk, message=Message.Signup, spaceId=space_data.id)
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")

def delete_space_controller(spaceId: int, db: Session, payload: PayloadSchema) -> ResponseWraper:
    try:
        space = db.get(Space, spaceId)
        print("Spcdjonsvkjvb ", space)
        print(payload, "This is payload")
        if not space:
            raise HTTPException(status_code=400, detail="Space Id not found")
        if space.user_id != payload['id']:
            raise HTTPException(status_code=400, detail="Invalid user")
        db.delete(space)
        db.commit()
        return ResponseWraper(status=Http.StatusOk, message=Message.DELETED, data="Deleted successfully")
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")
    
def get_all_spaces_controller(db: Session, payload: PayloadSchema) -> SpaceListWraper:
    try:
        statement = select(Space.id, Space.height, Space.width, Space.thumbnail, Space.name, Space.user_id).where(Space.user_id == payload['id'])
        result = db.exec(statement).all()
        print("Hi", result)
        return SpaceListWraper(status=Http.StatusOk, message=Message.ALL_FETCHED, spaces=result)
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")
    
def get_space_controller(spaceId: int, db: Session, payload: PayloadSchema) -> GetSpaceWraper:
    try:
        space = db.get(Space, spaceId)
        if not space:
            raise HTTPException(status_code=400, detail="Space Id not found")
        if space.user_id != payload['id']:
            raise HTTPException(status_code=400, detail="Invalid user")
        return GetSpaceWraper(status=200, message=Message.GET, height=space.height, width=space.width, elements=space.space_elements_list) 
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")
    

def add_an_element_controller(element: AddElementSchema, db: Session, payload: PayloadSchema) -> ResponseWraper:
    try:
        print("Element:, ", element)
        print("Space Id", element.spaceId) 
        space = db.get(Space, element.spaceId)
        print(space, "my space")
        if space.user_id != payload['id']:
            raise HTTPException(status_code=400, detail="User not eligible")
        if space.width <= element.x or space.height <= element.y:
            raise HTTPException(status_code=400, detail="Space not exist this much")
        print("jqdsvcud")
        # if space.element.x and space.element.y:
        #     raise HTTPException(status_code=400, detail="Already element present")
        #  one more check as it should be empty
        print("Jhandu bsm")
        space_element = SpaceElement.model_validate(element)        
        db.add(space_element)
        db.commit()
        db.refresh(space_element)
        return ResponseWraper(status=200, message=Message.CREATED, data = "Element added successfully")
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")
    

def delete_an_element_controller(id: int, db: Session, payload: PayloadSchema) -> ResponseWraper:
    try:
        space_element = db.get(SpaceElement, id)
        print("Spcdjonsvkjvb ", space_element)
        print(payload, "This is payload")
        if not space_element:
            raise HTTPException(status_code=400, detail="Space Id not found")
        if space_element.user_id != payload['id']:
            raise HTTPException(status_code=400, detail="Invalid user")
        db.delete(space_element)
        db.commit()
        return ResponseWraper(status=Http.StatusOk, message=Message.DELETED, data="Deleted successfully")
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")
    