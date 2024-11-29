from sqlmodel import Session, select
from utils.wraper import ResponseWraper, UserSchema, LoginUserSchema
from utils.status_code import Http, Message
from models.user import User
from utils.auth import auth_wrapper, get_password_hash, verify_password, encode_token, decode_token
from fastapi import HTTPException

def create_user_response(user: UserSchema, db: Session) -> ResponseWraper:
    try:
        result = select(User).where(User.username == user.username)
        statement = db.exec(result).first()
        if statement:
            raise HTTPException(status_code=400, detail="Already exist")
        hashed_password = get_password_hash(user.password)
        db_user = User.model_validate(user)
        db_user.password = hashed_password
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return ResponseWraper(status=Http.StatusOk, message=Message.Signup, data=db_user.id)
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Catch Error found")
    

def give_token(user: LoginUserSchema, db: Session) -> ResponseWraper:
    try:
        statement = select(User).where(User.username == user.username)
        result = db.exec(statement).first()
        if not result:
            raise HTTPException(status_code=403, detail="User not exist")
        verify_pass = verify_password(user.password, result.password)
        if not verify_pass:
            raise HTTPException(status_code=400, detail="Username or password is incorrect")
        token = encode_token(result.id, result.role)
        return ResponseWraper(status=Http.StatusOk, message=Message.Login, data=token)
    except HTTPException as http_err:
        raise http_err
    except Exception as error:
        raise HTTPException(status_code=500, detail="Catch Error found")
