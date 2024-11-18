from sqlmodel import Session, select
from utils.wraper import ResponseWraper, SpaceSchema, PayloadSchema
from utils.status_code import Http, Message
from models import User, Space
from utils.auth import auth_wrapper, get_password_hash, verify_password, encode_token, decode_token


def create_space_controller(space: SpaceSchema, db: Session, payload: PayloadSchema) -> ResponseWraper:
    try:
        print(payload, "payload")
        print(space, "space")
        if space.mapId:
            
            print("Tanmay")
        space_data = Space(name=space.name, width=space.width, height=space.height, user_id=payload['id'])
        return ResponseWraper(status=Http.StatusOk, message=Message.Signup, data="")
    except Exception as error:
        print(error)
        return ResponseWraper(status=Http.StatusInternalServerError, message=Message.CatchError, data="catch error in console")
