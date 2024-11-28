from fastapi import APIRouter, Depends, Query, HTTPException, params
from api.controllers.user import update_metadata_controller, get_all_avatars_controller, get_others_metadata_controller
from utils.wraper import ResponseWraper
from sqlmodel import Session
from db.config import get_session
from utils.auth import auth_wrapper

USER_ROUTES = APIRouter()


@USER_ROUTES.patch("/metadata", response_model=ResponseWraper)
def update_metadata(avatar_id: int, db: Session = Depends(get_session), payload = Depends(auth_wrapper)):
    try:
        response = update_metadata_controller(avatar_id, db, payload)
        return response
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        print(e)
        return e


@USER_ROUTES.get("/avatars", response_model=ResponseWraper)
def get_all_avatars(offset: int = 0, limit: int = Query(default = 10, le = 10), db: Session = Depends(get_session)):
    try:
        response = get_all_avatars_controller(offset, limit, db)
        return response
    except Exception as e:
        print(e)
        return e

@USER_ROUTES.get("/metadata/bulk", response_model=ResponseWraper)
def get_others_metadata(ids:str = Query(...), db: Session = Depends(get_session)):
    try:
        response = get_others_metadata_controller(ids, db)
        return response
    except Exception as e:
        print(e)
        return e