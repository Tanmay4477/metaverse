from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from models.user import User
    from models.space_element import SpaceElement

class Space(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    width: int
    height: int
    thumbnail: str | None
    user_id: int | None = Field(default=None, foreign_key="user.id")
    user_detail: Optional["User"] = Relationship(back_populates="spaces")
    space_elements_list: list["SpaceElement"] = Relationship(back_populates="space_list")

