from fastapi import APIRouter, Depends, HTTPException
from api.controllers.space import create_space_controller, delete_space_controller, get_all_spaces_controller
from utils.wraper import PostSpaceSchema, ResponseWraper, SpaceSchema, PayloadSchema, SpaceListWraper
from sqlmodel import Session
from db.config import get_session
from utils.auth import auth_wrapper

SPACE_ROUTES = APIRouter()

@SPACE_ROUTES.post("/", response_model=PostSpaceSchema)
def create_space(space: SpaceSchema, db: Session = Depends(get_session), payload: PayloadSchema = Depends(auth_wrapper)):
    try:
        response = create_space_controller(space, db, payload)
        return response
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")

@SPACE_ROUTES.delete("/{spaceId}", response_model=ResponseWraper)
def delete_space(spaceId: int, db: Session = Depends(get_session), payload: PayloadSchema = Depends(auth_wrapper)):
    try:
        response = delete_space_controller(spaceId, db, payload)
        return response
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")

@SPACE_ROUTES.get("/all", response_model=SpaceListWraper)
def get_all_spaces(db: Session = Depends(get_session), payload: PayloadSchema = Depends(auth_wrapper)):
    try:
        value = get_all_spaces_controller(db, payload)
        return value
    except Exception as e:
        print(e)
        return e


