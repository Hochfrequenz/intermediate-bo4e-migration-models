import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import ARRAY, Column, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.bilanzierungsmethode import Bilanzierungsmethode
from ibims.orm.models.enum.dienstleistungstyp import Dienstleistungstyp
from ibims.orm.models.enum.netzebene import Netzebene
from ibims.orm.models.enum.preisstatus import Preisstatus
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import (
    PreisblattHardwareinklusiveGeraeteLink,
    PreisblattHardwarepreispositionenLink,
    PreisblattHardwarezusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.geraet import Geraet
    from ibims.orm.models.bo.marktteilnehmer import Marktteilnehmer
    from ibims.orm.models.com.preisposition import Preisposition
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class PreisblattHardware(SQLModel, table=True):
    """
    Variante des Preisblattmodells zur Abbildung der Preise für zusätzliche Hardware

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattHardware.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattHardware JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/PreisblattHardware.json>`_
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
    Eine Bezeichnung für das Preisblatt
    """
    preisblatthardware_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ | None = Field(Typ.PREISBLATTHARDWARE)
    basisgeraet_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("geraet.geraet_sqlid", ondelete="SET NULL"))
    )
    basisgeraet: "Geraet" = Relationship(
        back_populates="preisblatthardware_basisgeraet",
        sa_relationship_kwargs={"foreign_keys": "[PreisblattHardware.basisgeraet_id]"},
    )
    bilanzierungsmethode: Bilanzierungsmethode | None = Field(None)
    gueltigkeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    gueltigkeit: "Zeitraum" = Relationship(
        back_populates="preisblatthardware_gueltigkeit",
        sa_relationship_kwargs={"foreign_keys": "[PreisblattHardware.gueltigkeit_id]"},
    )
    herausgeber_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktteilnehmer.marktteilnehmer_sqlid", ondelete="SET NULL"),
        )
    )
    herausgeber: "Marktteilnehmer" = Relationship(
        back_populates="preisblatthardware_herausgeber",
        sa_relationship_kwargs={"foreign_keys": "[PreisblattHardware.herausgeber_id]"},
    )
    inklusiveDienstleistungen: List[Dienstleistungstyp] | None = Field(
        None,
        sa_column=Column(ARRAY(Enum(Dienstleistungstyp, name="dienstleistungstyp"))),
    )
    inklusiveGeraete: List["Geraet"] = Relationship(
        back_populates="preisblatthardware_inklusivegeraete_link",
        link_model=PreisblattHardwareinklusiveGeraeteLink,
    )
    messebene: Netzebene | None = Field(None)
    preispositionen: List["Preisposition"] = Relationship(
        back_populates="preisblatthardware_preispositionen_link",
        link_model=PreisblattHardwarepreispositionenLink,
    )
    preisstatus: Preisstatus | None = Field(None)
    sparte: Sparte | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="preisblatthardware_zusatzattribute_link",
        link_model=PreisblattHardwarezusatzAttributeLink,
    )
