from sqlmodel import Session, select
from utils.wraper import AllElementsWraper
from utils.status_code import Http, Message
from models import Element

def all_elements_controller(db: Session) -> AllElementsWraper:
    try:
        statement = select(Element)
        result = db.exec(statement).all()
        return AllElementsWraper(status=Http.StatusOk, message=Message.Signup, elements=result)
    except Exception as error:
        print(error)
        return AllElementsWraper(status=Http.StatusInternalServerError, message=Message.CatchError, elements="Something went wrong")
    
