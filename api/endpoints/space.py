from fastapi import APIRouter, Depends
from api.controllers.space import create_space_controller
from utils.wraper import ResponseWraper, SpaceSchema, PayloadSchema
from sqlmodel import Session
from db.config import get_session
from utils.auth import auth_wrapper

SPACE_ROUTES = APIRouter()

@SPACE_ROUTES.post("/", response_model=ResponseWraper)
def create_space(space: SpaceSchema, db: Session = Depends(get_session), payload: PayloadSchema = Depends(auth_wrapper)):
    try:
        response = create_space_controller(space, db, payload)
        return response
    except Exception as e:
        print(e)
        return e

# @SPACE_ROUTES.delete("/{spaceId}", response_model=ResponseWraper)
# def delete_space(user: UserSchema, db: Session = Depends(get_session)):
#     try:
#         response = create_user_response(user, db)
#         return response
#     except Exception as e:
#         print(e)
#         return e

# @SPACE_ROUTES.get("/all", response_model=ResponseWraper)
# def get_all_spaces(user: UserSchema, db: Session = Depends(get_session)):
#     try:
#         value = give_token(user, db)
#         return value
#     except Exception as e:
#         print(e)
#         return e


