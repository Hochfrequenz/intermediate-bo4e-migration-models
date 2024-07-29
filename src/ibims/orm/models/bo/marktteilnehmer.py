import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import ARRAY, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.marktrolle import Marktrolle
from ibims.orm.models.enum.rollencodetyp import Rollencodetyp
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import MarktteilnehmerzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.bo.preisblatt import Preisblatt
    from ibims.orm.models.bo.preisblatt_dienstleistung import PreisblattDienstleistung
    from ibims.orm.models.bo.preisblatt_hardware import PreisblattHardware
    from ibims.orm.models.bo.preisblatt_konzessionsabgabe import PreisblattKonzessionsabgabe
    from ibims.orm.models.bo.preisblatt_messung import PreisblattMessung
    from ibims.orm.models.bo.preisblatt_netznutzung import PreisblattNetznutzung
    from ibims.orm.models.bo.regionaltarif import Regionaltarif
    from ibims.orm.models.bo.tarif import Tarif
    from ibims.orm.models.bo.tarifinfo import Tarifinfo
    from ibims.orm.models.bo.tarifkosten import Tarifkosten
    from ibims.orm.models.bo.tarifpreisblatt import Tarifpreisblatt
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Marktteilnehmer(SQLModel, table=True):
    """
    Objekt zur Aufnahme der Information zu einem Marktteilnehmer

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Marktteilnehmer.svg" type="image/svg+xml"></object>

    .. HINT::
        `Marktteilnehmer JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Marktteilnehmer.json>`_
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
    rollencodenummer: str | None = Field(default=None, title="Rollencodenummer")
    """
    Gibt die Codenummer der Marktrolle an
    """
    marktteilnehmer_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ | None = Field(Typ.MARKTTEILNEHMER)
    geschaeftspartner_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="SET NULL"),
        )
    )
    geschaeftspartner: "Geschaeftspartner" = Relationship(
        back_populates="marktteilnehmer_geschaeftspartner",
        sa_relationship_kwargs={"foreign_keys": "[Marktteilnehmer.geschaeftspartner_id]"},
    )
    makoadresse: List[str] | None = Field(None, title="makoadresse", sa_column=Column(ARRAY(String)))
    marktrolle: Marktrolle | None = Field(None)
    rollencodetyp: Rollencodetyp | None = Field(None)
    sparte: Sparte | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="marktteilnehmer_zusatzattribute_link",
        link_model=MarktteilnehmerzusatzAttributeLink,
    )
    preisblatt_herausgeber: List["Preisblatt"] = Relationship(
        back_populates="herausgeber",
        sa_relationship_kwargs={
            "primaryjoin": "Preisblatt.herausgeber_id==Marktteilnehmer.marktteilnehmer_sqlid",
            "lazy": "joined",
        },
    )
    preisblattdienstleistung_herausgeber: List["PreisblattDienstleistung"] = Relationship(
        back_populates="herausgeber",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattDienstleistung.herausgeber_id==Marktteilnehmer.marktteilnehmer_sqlid",
            "lazy": "joined",
        },
    )
    preisblatthardware_herausgeber: List["PreisblattHardware"] = Relationship(
        back_populates="herausgeber",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattHardware.herausgeber_id==Marktteilnehmer.marktteilnehmer_sqlid",
            "lazy": "joined",
        },
    )
    preisblattkonzessionsabgabe_herausgeber: List["PreisblattKonzessionsabgabe"] = Relationship(
        back_populates="herausgeber",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattKonzessionsabgabe.herausgeber_id==Marktteilnehmer.marktteilnehmer_sqlid",
            "lazy": "joined",
        },
    )
    preisblattmessung_herausgeber: List["PreisblattMessung"] = Relationship(
        back_populates="herausgeber",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattMessung.herausgeber_id==Marktteilnehmer.marktteilnehmer_sqlid",
            "lazy": "joined",
        },
    )
    preisblattnetznutzung_herausgeber: List["PreisblattNetznutzung"] = Relationship(
        back_populates="herausgeber",
        sa_relationship_kwargs={
            "primaryjoin": "PreisblattNetznutzung.herausgeber_id==Marktteilnehmer.marktteilnehmer_sqlid",
            "lazy": "joined",
        },
    )
    regionaltarif_anbieter: List["Regionaltarif"] = Relationship(
        back_populates="anbieter",
        sa_relationship_kwargs={
            "primaryjoin": "Regionaltarif.anbieter_id==Marktteilnehmer.marktteilnehmer_sqlid",
            "lazy": "joined",
        },
    )
    tarif_anbieter: List["Tarif"] = Relationship(
        back_populates="anbieter",
        sa_relationship_kwargs={
            "primaryjoin": "Tarif.anbieter_id==Marktteilnehmer.marktteilnehmer_sqlid",
            "lazy": "joined",
        },
    )
    tarifinfo_anbieter: List["Tarifinfo"] = Relationship(
        back_populates="anbieter",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifinfo.anbieter_id==Marktteilnehmer.marktteilnehmer_sqlid",
            "lazy": "joined",
        },
    )
    tarifkosten_anbieter: List["Tarifkosten"] = Relationship(
        back_populates="anbieter",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifkosten.anbieter_id==Marktteilnehmer.marktteilnehmer_sqlid",
            "lazy": "joined",
        },
    )
    tarifpreisblatt_anbieter: List["Tarifpreisblatt"] = Relationship(
        back_populates="anbieter",
        sa_relationship_kwargs={
            "primaryjoin": "Tarifpreisblatt.anbieter_id==Marktteilnehmer.marktteilnehmer_sqlid",
            "lazy": "joined",
        },
    )
