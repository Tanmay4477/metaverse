from fastapi import APIRouter, Depends
from api.controllers.auth import create_user_response, give_token
from utils.wraper import ResponseWraper, UserSchema
from sqlmodel import Session
from db.config import get_session
from fastapi import HTTPException


AUTH_ROUTES = APIRouter()

@AUTH_ROUTES.post("/signup", response_model=ResponseWraper)
def create_user_admin(user: UserSchema, db: Session = Depends(get_session)):
    try:
        response = create_user_response(user, db)
        return response
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail="Catch Error found")


@AUTH_ROUTES.post("/signin", response_model=ResponseWraper)
def login_user(user: UserSchema, db: Session = Depends(get_session)):
    try:
        value = give_token(user, db)
        return value
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail="Catch Error found")


