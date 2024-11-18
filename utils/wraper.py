from pydantic import BaseModel, Field
from enum import Enum
from models import User, Avatar
from typing import List

class Avatars(BaseModel):
    id: int
    image_url: str
    name: str

class LoginUserSchema(BaseModel):
    username: str
    password: str

class ElementSchema(BaseModel):
    width: int
    height: int
    static: bool
    image_url: str
    name: str

class UpdateElementSchema(BaseModel):
    image_url: str

class SpaceElementSchema(BaseModel):
    id: int
    x: int
    y: int

class MapSchema(BaseModel): 
    name: str
    width: int
    height: int
    thumbnail: str
    defaultElements: List[SpaceElementSchema] = []

class AvatarSchema(BaseModel):
    id: int
    image_url: int

class ResponseWraper(BaseModel):
    status: int
    message: str
    data: None | str | User | int | List[Avatar] | List[AvatarSchema]

class Role(str, Enum):
    User = "user"
    Admin = "admin"

class getBulkMetadataParams(BaseModel):
    ids: list[int]

class UserSchema(BaseModel):
    username: str
    password: str
    role: Role = Field(default=Role.User)

class SpaceSchema(BaseModel):
    name: str
    width: int
    height: int
    mapId: int | None

class PayloadSchema(BaseModel):
    id: int
    role: str
    iat: int
    exp: int



