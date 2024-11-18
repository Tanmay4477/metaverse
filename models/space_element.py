from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from models import Space
    from models import Element


class SpaceElement(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    x: int
    y: int
    space_id: int | None = Field(default=None, foreign_key="space.id")
    space_list: Optional["Space"] = Relationship(back_populates="space_elements_list")
    element_id: int | None = Field(default=None, foreign_key="element.id")
    element_list: Optional["Element"] = Relationship(back_populates="space_elements_list")