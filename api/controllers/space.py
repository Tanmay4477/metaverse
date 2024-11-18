from sqlmodel import Session, select
from utils.wraper import ResponseWraper, SpaceSchema, PayloadSchema, PostSpaceSchema, SpaceListWraper
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
            # need to do somethin
            print("fdkjbhlfb")
            statement = select(SpaceElement).where(SpaceElement.space_id == map.id)
            result = db.exec(statement).all()
            print("resu", result)
            print("OLD SPACE ELEMENT")
            new_space_element = SpaceElement(result)
            #  Do something
            print("Lets see", new_space_element)
            space_data = Space(name=space.name, width=space.width or map.width, height=space.width or map.width, thumbnail=map.thumbnail, user_id=payload['id'])
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