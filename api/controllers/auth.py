from sqlmodel import Session, select
from utils.wraper import ResponseWraper, UserSchema, LoginUserSchema
from utils.status_code import Http, Message
from models.user import User
from utils.auth import auth_wrapper, get_password_hash, verify_password, encode_token, decode_token

def create_user_response(user: UserSchema, db: Session) -> ResponseWraper:
    try:
        result = select(User).where(User.username == user.username)
        statement = db.exec(result).first()
        if statement:
            return ResponseWraper(status=Http.StatusBadRequest, message=Message.AlreadyExist, data="")
        hashed_password = get_password_hash(user.password)
        db_user = User.model_validate(user)
        db_user.password = hashed_password
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return ResponseWraper(status=Http.StatusOk, message=Message.Signup, data=db_user.id)
    except Exception as error:
        print(error)
        return ResponseWraper(status=Http.StatusInternalServerError, message=Message.CatchError, data="catch error in console")
    

def give_token(user: LoginUserSchema, db: Session) -> ResponseWraper:
    try:
        statement = select(User).where(User.username == user.username)
        result = db.exec(statement).first()
        if not result:
            return ResponseWraper(status=Http.StatusForbidden, message=Message.UserNotExist, data="")
        verify_pass = verify_password(user.password, result.password)
        if not verify_pass:
            return ResponseWraper(status=Http.StatusBadRequest, message=Message.NotMatch, data="Try again")
        token = encode_token(result.id, result.role)
        return ResponseWraper(status=Http.StatusOk, message=Message.Login, data=token)
    except Exception as error:
        print(error)
        return error

