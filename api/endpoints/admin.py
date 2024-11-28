from fastapi import APIRouter, Depends
from api.controllers.admin import create_element_controller, update_element_controller, create_map_controller, create_avatar_controller
from utils.wraper import ResponseWraper, ElementSchema, MapSchema, UpdateElementSchema, CreateAvatar
from sqlmodel import Session
from db.config import get_session
from utils.auth import auth_wrapper

ADMIN_ROUTES = APIRouter()

@ADMIN_ROUTES.post("/element", response_model=ResponseWraper)
def create_element(element: ElementSchema, db: Session = Depends(get_session), payload = Depends(auth_wrapper)):
    try:
        response = create_element_controller(element, db, payload)
        return response
    except Exception as e:
        print(e)
        return e

@ADMIN_ROUTES.patch("/element/{elementId}", response_model=ResponseWraper)
def update_element(element: UpdateElementSchema, elementId: int, db: Session = Depends(get_session), payload = Depends(auth_wrapper)):
    try:
        value = update_element_controller(elementId, element, db, payload)
        return value
    except Exception as e:
        print(e)
        return e


@ADMIN_ROUTES.post("/map", response_model=ResponseWraper)
def create_map(map: MapSchema, db: Session = Depends(get_session), payload = Depends(auth_wrapper)):
    try:
        value = create_map_controller(map, db, payload)
        return value
    except Exception as e:
        print(e)
        return e


@ADMIN_ROUTES.post("/avatar", response_model=ResponseWraper)
def create_avatar(avatar: CreateAvatar, db: Session = Depends(get_session), payload = Depends(auth_wrapper)):
    print('fdlvnsdkj bsk')
    try:
        print("kjbnvkjdf")
        value = create_avatar_controller(avatar, db, payload)
        return value
    except Exception as e:
        print(e)
        return e

    
