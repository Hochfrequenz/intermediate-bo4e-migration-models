import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, Any, List

from pydantic import ConfigDict
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.hinweis_thema import HinweisThema
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import HinweiszusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Hinweis(SQLModel, table=True):
    """
    Contains specific hints for the handling of contracts and customers.
    Hints are meant to be read and written by agents or customer service employees.
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    id: str | None = Field(default=None, alias="_id", title=" Id")
    erstellungsdatum: datetime = Field(..., title="Erstellungsdatum")
    nachricht: str = Field(..., title="Nachricht")
    hinweis_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    typ: Typ = Field(Typ.HINWEIS)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="hinweis_zusatzattribute_link",
        link_model=HinweiszusatzAttributeLink,
    )
    thema: HinweisThema = Field(None)
