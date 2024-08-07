import uuid as uuid_pkg
from typing import TYPE_CHECKING, Any, List

from pydantic import ConfigDict
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import KampagnezusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Kampagne(SQLModel, table=True):
    """
    A "Kampagne"/campaign models which marketing activities led customers to a product/tariff.
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    id: str = Field(..., title="Id")
    name: str = Field(..., title="Name")
    kampagne_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    typ: Typ = Field(Typ.KAMPAGNE)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="kampagne_zusatzattribute_link",
        link_model=KampagnezusatzAttributeLink,
    )
