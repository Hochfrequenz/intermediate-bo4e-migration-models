import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.netzebene import Netzebene
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import (
    MesslokationgeraeteLink,
    MesslokationmessdienstleistungLink,
    MesslokationmesslokationszaehlerLink,
    MesslokationzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.geraet import Geraet
    from ibims.orm.models.bo.lastgang import Lastgang
    from ibims.orm.models.bo.rechnung import Rechnung
    from ibims.orm.models.bo.zaehler import Zaehler
    from ibims.orm.models.com.adresse import Adresse
    from ibims.orm.models.com.dienstleistung import Dienstleistung
    from ibims.orm.models.com.geokoordinaten import Geokoordinaten
    from ibims.orm.models.com.katasteradresse import Katasteradresse
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Messlokation(SQLModel, table=True):
    """
    Object containing information about a Messlokation

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Messlokation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Messlokation.json>`_
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
    grundzustaendiger_msb_codenr: str | None = Field(
        default=None,
        alias="grundzustaendigerMsbCodenr",
        title="Grundzustaendigermsbcodenr",
    )
    """
    grundzustaendiger_msbim_codenr: Optional[str] = None
    """
    grundzustaendiger_msbim_codenr: str | None = Field(
        default=None,
        alias="grundzustaendigerMsbimCodenr",
        title="Grundzustaendigermsbimcodenr",
    )
    """
    # only one of the following three optional address attributes can be set
    messadresse: Optional["Adresse"] = None
    """
    messgebietnr: str | None = Field(default=None, title="Messgebietnr")
    """
    Die Nummer des Messgebietes in der ene't-Datenbank
    """
    messlokations_id: str | None = Field(default=None, alias="messlokationsId", title="Messlokationsid")
    """
    Die Messlokations-Identifikation; Das ist die frühere Zählpunktbezeichnung
    """
    messlokation_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    lastgang_messlokation: List["Lastgang"] = Relationship(
        back_populates="messlokation",
        sa_relationship_kwargs={
            "primaryjoin": "Lastgang.messlokation_id==Messlokation.messlokation_sqlid",
            "lazy": "joined",
        },
    )
    typ: Typ | None = Field(Typ.MESSLOKATION)
    geoadresse_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geokoordinaten.geokoordinaten_sqlid", ondelete="SET NULL"),
        )
    )
    geoadresse: "Geokoordinaten" = Relationship(
        back_populates="messlokation_geoadresse",
        sa_relationship_kwargs={"foreign_keys": "[Messlokation.geoadresse_id]"},
    )
    geraete: List["Geraet"] = Relationship(
        back_populates="messlokation_geraete_link", link_model=MesslokationgeraeteLink
    )
    katasterinformation_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("katasteradresse.katasteradresse_sqlid", ondelete="SET NULL"),
        )
    )
    katasterinformation: "Katasteradresse" = Relationship(
        back_populates="messlokation_katasterinformation",
        sa_relationship_kwargs={"foreign_keys": "[Messlokation.katasterinformation_id]"},
    )
    messadresse_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("adresse.adresse_sqlid", ondelete="SET NULL"))
    )
    messadresse: "Adresse" = Relationship(
        back_populates="messlokation_messadresse",
        sa_relationship_kwargs={"foreign_keys": "[Messlokation.messadresse_id]"},
    )
    messdienstleistung: List["Dienstleistung"] = Relationship(
        back_populates="messlokation_messdienstleistung_link",
        link_model=MesslokationmessdienstleistungLink,
    )
    messlokationszaehler: List["Zaehler"] = Relationship(
        back_populates="messlokation_messlokationszaehler_link",
        link_model=MesslokationmesslokationszaehlerLink,
    )
    netzebeneMessung: Netzebene | None = Field(None)
    sparte: Sparte | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="messlokation_zusatzattribute_link",
        link_model=MesslokationzusatzAttributeLink,
    )
    rechnung_messlokation: List["Rechnung"] = Relationship(
        back_populates="messlokation",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnung.messlokation_id==Messlokation.messlokation_sqlid",
            "lazy": "joined",
        },
    )
