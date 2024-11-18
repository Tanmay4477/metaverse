from sqlmodel import Session, select
from utils.wraper import ResponseWraper, AvatarSchema
from utils.status_code import Http, Message
from models.user import User
from models.avatar import Avatar
from utils.auth import auth_wrapper, get_password_hash, verify_password, encode_token, decode_token
from fastapi import HTTPException
import ast

def update_metadata_controller(avatar_id: int, db: Session, payload):
    try:
        user_id = payload['id']
        user = db.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        avatar_exist = db.get(Avatar, avatar_id)
        if avatar_exist is None:
            raise HTTPException(status_code=404, detail="Avatar not found")

        user.avatar_id = avatar_id
        db.add(user)
        db.commit()
        db.refresh(user)
        print("user", user)
        return ResponseWraper(status=Http.StatusOk, message=Message.UPDATED, data="Changed")
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")
    
    
def get_all_avatars_controller(offset, limit, db: Session) -> ResponseWraper:
    try:
        avatars = db.exec(select(Avatar).offset(offset).limit(limit)).all()
        return ResponseWraper(status=Http.StatusOk, message=Message.ALL_FETCHED, data=avatars)
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")
    
def get_others_metadata_controller(ids: list[int], db: Session) -> ResponseWraper:
    try:
        idList = ast.literal_eval(ids)
        print("Yhis is come sonc")
        statement = select(User).where(User.id.in_(idList))
        print("Yhis is come ", statement)
        result = db.exec(statement).all()
        print("Yhis is kjvbidkjxbdfj ", result)
        avatars = [User(user_id = user.id, image_url=user.avatar_list.image_url) for user in result]
        print({"fgnmntsfnsfg": avatars})
        return ResponseWraper(status=Http.StatusOk, message=Message.ALL_FETCHED, data="hi")
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error Found")

    
