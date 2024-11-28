from fastapi import APIRouter, Depends, HTTPException
from api.controllers.space import create_space_controller, delete_space_controller, get_all_spaces_controller, get_space_controller, add_an_element_controller, delete_an_element_controller
from utils.wraper import PostSpaceSchema, ResponseWraper, SpaceSchema, PayloadSchema, SpaceListWraper, GetSpaceWraper, AddElementSchema
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
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")


@SPACE_ROUTES.get("/{spaceId}", response_model=GetSpaceWraper)
def get_space(spaceId: int, db: Session = Depends(get_session), payload: PayloadSchema = Depends(auth_wrapper)):
    try:
        response = get_space_controller(spaceId, db, payload)
        return response
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")


@SPACE_ROUTES.post("/element", response_model=ResponseWraper)
def add_an_element(element: AddElementSchema, db: Session = Depends(get_session), payload: PayloadSchema = Depends(auth_wrapper)):
    try:
        response = add_an_element_controller(element, db, payload)
        return response
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")


@SPACE_ROUTES.delete("/element/{id1}", response_model=ResponseWraper)
def delete_an_element(id1: int, db: Session = Depends(get_session), payload: PayloadSchema = Depends(auth_wrapper)):
    try:
        response = delete_an_element_controller(id1, db, payload)
        return response
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")

