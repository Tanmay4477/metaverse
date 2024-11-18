from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import SpaceElement


class Element(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    width: int
    height: int
    static: bool
    image_url: str
    space_elements_list: list["SpaceElement"] = Relationship(back_populates="element_list")