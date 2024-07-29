import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import (
    Buendelvertragunterzeichnervp1Link,
    Buendelvertragunterzeichnervp2Link,
    UnterschriftzusatzAttributeLink,
    Vertragunterzeichnervp1Link,
    Vertragunterzeichnervp2Link,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.buendelvertrag import Buendelvertrag
    from ibims.orm.models.bo.vertrag import Vertrag
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Unterschrift(SQLModel, table=True):
    """
    Modellierung einer Unterschrift, z.B. für Verträge, Angebote etc.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Unterschrift.svg" type="image/svg+xml"></object>

    .. HINT::
        `Unterschrift JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Unterschrift.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = None

    # pylint: disable=duplicate-code
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        extra="allow",
        # json_encoders is deprecated, but there is no easy-to-use alternative. The best way would be to create
        # an annotated version of Decimal, but you would have to use it everywhere in the pydantic models.
        # See this issue for more info: https://github.com/pydantic/pydantic/issues/6375
        json_encoders={Decimal: str},
    )
    """
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    datum: datetime | None = Field(default=None, title="Datum")
    """
    Ort, an dem die Unterschrift geleistet wird
    """
    name: str | None = Field(default=None, title="Name")
    """
    Name des Unterschreibers
    """
    ort: str | None = Field(default=None, title="Ort")
    """
    Ort, an dem die Unterschrift geleistet wird
    """
    unterschrift_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    buendelvertrag_unterzeichnervp1_link: List["Buendelvertrag"] = Relationship(
        back_populates="unterzeichnervp1", link_model=Buendelvertragunterzeichnervp1Link
    )
    buendelvertrag_unterzeichnervp2_link: List["Buendelvertrag"] = Relationship(
        back_populates="unterzeichnervp2", link_model=Buendelvertragunterzeichnervp2Link
    )
    vertrag_unterzeichnervp1_link: List["Vertrag"] = Relationship(
        back_populates="unterzeichnervp1", link_model=Vertragunterzeichnervp1Link
    )
    vertrag_unterzeichnervp2_link: List["Vertrag"] = Relationship(
        back_populates="unterzeichnervp2", link_model=Vertragunterzeichnervp2Link
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="unterschrift_zusatzattribute_link",
        link_model=UnterschriftzusatzAttributeLink,
    )
