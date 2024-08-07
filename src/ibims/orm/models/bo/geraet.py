import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.geraeteklasse import Geraeteklasse
from ibims.orm.models.enum.geraetetyp import Geraetetyp
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import (
    GeraetzusatzAttributeLink,
    MesslokationgeraeteLink,
    PreisblattHardwareinklusiveGeraeteLink,
    PreisblattMessunginklusiveGeraeteLink,
    TarifeinschraenkungeinschraenkungzaehlerLink,
    ZaehlergeraeteLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.messlokation import Messlokation
    from ibims.orm.models.bo.preisblatt_dienstleistung import PreisblattDienstleistung
    from ibims.orm.models.bo.preisblatt_hardware import PreisblattHardware
    from ibims.orm.models.bo.preisblatt_messung import PreisblattMessung
    from ibims.orm.models.bo.zaehler import Zaehler
    from ibims.orm.models.com.tarifeinschraenkung import Tarifeinschraenkung
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Geraet(SQLModel, table=True):
    """
    Mit diesem BO werden alle Geräte modelliert, die keine Zähler sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geraet.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geraet JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Geraet.json>`_
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
    Bezeichnung des Geräts
    """
    geraetenummer: str | None = Field(default=None, title="Geraetenummer")
    """
    Die auf dem Gerät aufgedruckte Nummer, die vom MSB vergeben wird.
    """
    geraet_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    typ: Typ | None = Field(Typ.GERAET)
    geraeteklasse: Geraeteklasse | None = Field(None)
    geraetetyp: Geraetetyp | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="geraet_zusatzattribute_link",
        link_model=GeraetzusatzAttributeLink,
    )
    messlokation_geraete_link: List["Messlokation"] = Relationship(
        back_populates="geraete", link_model=MesslokationgeraeteLink
    )
    preisblattdienstleistung_geraetedetails: List["PreisblattDienstleistung"] = Relationship(
        back_populates="geraetedetails",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattDienstleistung.geraetedetails_id==Geraet.geraet_sqlid",
            "lazy": "joined",
        },
    )
    preisblatthardware_basisgeraet: List["PreisblattHardware"] = Relationship(
        back_populates="basisgeraet",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattHardware.basisgeraet_id==Geraet.geraet_sqlid",
            "lazy": "joined",
        },
    )
    preisblatthardware_inklusivegeraete_link: List["PreisblattHardware"] = Relationship(
        back_populates="inklusiveGeraete",
        link_model=PreisblattHardwareinklusiveGeraeteLink,
    )
    preisblattmessung_inklusivegeraete_link: List["PreisblattMessung"] = Relationship(
        back_populates="inklusiveGeraete",
        link_model=PreisblattMessunginklusiveGeraeteLink,
    )
    zaehler_geraete_link: List["Zaehler"] = Relationship(back_populates="geraete", link_model=ZaehlergeraeteLink)
    tarifeinschraenkung_einschraenkungzaehler_link: List["Tarifeinschraenkung"] = Relationship(
        back_populates="einschraenkungzaehler",
        link_model=TarifeinschraenkungeinschraenkungzaehlerLink,
    )
