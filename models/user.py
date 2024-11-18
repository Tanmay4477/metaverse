from sqlmodel import Relationship, SQLModel, Field
from enum import Enum
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from models.avatar import Avatar
    from models.space import Space

class Role(str, Enum):
    User = "user"
    Admin = "admin"

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    role: Role | None = Field(default=Role.User)
    spaces: list["Space"] = Relationship(back_populates="user_detail")
    avatar_id: int | None = Field(default=None, foreign_key="avatar.id")
    avatar_list: Optional["Avatar"] = Relationship(back_populates="users_list")