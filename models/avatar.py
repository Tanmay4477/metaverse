from sqlmodel import Relationship, SQLModel, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User

class Avatar(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    image_url: str | None
    name: str | None
    users_list: list["User"] = Relationship(back_populates="avatar_list")
    