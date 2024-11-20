from fastapi import APIRouter, Depends
from api.controllers.arena import all_elements_controller
from utils.wraper import AllElementsWraper
from sqlmodel import Session
from db.config import get_session

ARENA_ROUTES = APIRouter()

@ARENA_ROUTES.get("/", response_model=AllElementsWraper)
def all_elements(db: Session = Depends(get_session)):
    try:
        response = all_elements_controller(db)
        return response
    except Exception as e:
        print(e)
        return e


