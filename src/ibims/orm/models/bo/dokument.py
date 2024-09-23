import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, Any, List

from pydantic import ConfigDict
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import DokumentzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Dokument(SQLModel, table=True):
    """
    A generic document reference like for bills, order confirmations and cancellations
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    id: str | None = Field(default=None, alias="_id", title=" Id")
    erstellungsdatum: datetime = Field(..., title="Erstellungsdatum")
    has_been_sent: bool = Field(..., alias="hasBeenSent", title="Hasbeensent")
    dokumentenname: str = Field(..., title="Dokumentenname")
    vorlagenname: str = Field(..., title="Vorlagenname")
    dokument_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    typ: Typ = Field(Typ.DOKUMENT)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="dokument_zusatzattribute_link",
        link_model=DokumentzusatzAttributeLink,
    )
