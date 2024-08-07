import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import RegionnegativListeLink, RegionpositivListeLink, RegionzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.regionskriterium import Regionskriterium
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Region(SQLModel, table=True):
    """
    Modellierung einer Region als Menge von Kriterien, die eine Region beschreiben

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Region.svg" type="image/svg+xml"></object>

    .. HINT::
        `Region JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Region.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Bezeichnung der Region
    """
    region_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    typ: Typ | None = Field(Typ.REGION)
    negativListe: List["Regionskriterium"] = Relationship(
        back_populates="region_negativliste_link", link_model=RegionnegativListeLink
    )
    positivListe: List["Regionskriterium"] = Relationship(
        back_populates="region_positivliste_link", link_model=RegionpositivListeLink
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="region_zusatzattribute_link",
        link_model=RegionzusatzAttributeLink,
    )
