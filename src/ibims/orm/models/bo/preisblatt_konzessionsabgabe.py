import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.kundengruppe_ka import KundengruppeKA
from ibims.orm.models.enum.preisstatus import Preisstatus
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import (
    PreisblattKonzessionsabgabepreispositionenLink,
    PreisblattKonzessionsabgabezusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.marktteilnehmer import Marktteilnehmer
    from ibims.orm.models.com.preisposition import Preisposition
    from ibims.orm.models.com.zeitraum import Zeitraum
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class PreisblattKonzessionsabgabe(SQLModel, table=True):
    """
    Die Variante des Preisblattmodells zur Abbildung von allgemeinen Abgaben

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattKonzessionsabgabe.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattKonzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/PreisblattKonzessionsabgabe.json>`_
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
    preisblattkonzessionsabgabe_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ | None = Field(Typ.PREISBLATTKONZESSIONSABGABE)
    gueltigkeit_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitraum.zeitraum_sqlid", ondelete="SET NULL"),
        )
    )
    gueltigkeit: "Zeitraum" = Relationship(
        back_populates="preisblattkonzessionsabgabe_gueltigkeit",
        sa_relationship_kwargs={"foreign_keys": "[PreisblattKonzessionsabgabe.gueltigkeit_id]"},
    )
    herausgeber_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("marktteilnehmer.marktteilnehmer_sqlid", ondelete="SET NULL"),
        )
    )
    herausgeber: "Marktteilnehmer" = Relationship(
        back_populates="preisblattkonzessionsabgabe_herausgeber",
        sa_relationship_kwargs={"foreign_keys": "[PreisblattKonzessionsabgabe.herausgeber_id]"},
    )
    kundengruppeKA: KundengruppeKA | None = Field(None)
    preispositionen: List["Preisposition"] = Relationship(
        back_populates="preisblattkonzessionsabgabe_preispositionen_link",
        link_model=PreisblattKonzessionsabgabepreispositionenLink,
    )
    preisstatus: Preisstatus | None = Field(None)
    sparte: Sparte | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="preisblattkonzessionsabgabe_zusatzattribute_link",
        link_model=PreisblattKonzessionsabgabezusatzAttributeLink,
    )
