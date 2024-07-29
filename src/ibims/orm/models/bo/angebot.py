import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import AngebotvariantenLink, AngebotzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.bo.person import Person
    from ibims.orm.models.com.angebotsvariante import Angebotsvariante
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Angebot(SQLModel, table=True):
    """
    Mit diesem BO kann ein Versorgungsangebot zur Strom- oder Gasversorgung oder die Teilnahme an einer Ausschreibung
    übertragen werden. Es können verschiedene Varianten enthalten sein (z.B. ein- und mehrjährige Laufzeit).
    Innerhalb jeder Variante können Teile enthalten sein, die jeweils für eine oder mehrere Marktlokationen erstellt
    werden.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Angebot.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebot JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Angebot.json>`_
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
    anfragereferenz: str | None = Field(default=None, title="Anfragereferenz")
    """
    Bis zu diesem Zeitpunkt (Tag/Uhrzeit) inklusive gilt das Angebot
    """
    angebotsdatum: datetime | None = Field(default=None, title="Angebotsdatum")
    """
    Erstellungsdatum des Angebots
    """
    angebotsnummer: str | None = Field(default=None, title="Angebotsnummer")
    """
    Eindeutige Nummer des Angebotes
    """
    bindefrist: datetime | None = Field(default=None, title="Bindefrist")
    """
    Bis zu diesem Zeitpunkt (Tag/Uhrzeit) inklusive gilt das Angebot
    """
    angebot_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    typ: Typ | None = Field(Typ.ANGEBOT)
    angebotsgeber_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="SET NULL"),
        )
    )
    angebotsgeber: "Geschaeftspartner" = Relationship(
        back_populates="angebot_angebotsgeber",
        sa_relationship_kwargs={"foreign_keys": "[Angebot.angebotsgeber_id]"},
    )
    angebotsnehmer_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("geschaeftspartner.geschaeftspartner_sqlid", ondelete="SET NULL"),
        )
    )
    angebotsnehmer: "Geschaeftspartner" = Relationship(
        back_populates="angebot_angebotsnehmer",
        sa_relationship_kwargs={"foreign_keys": "[Angebot.angebotsnehmer_id]"},
    )
    sparte: Sparte | None = Field(None)
    unterzeichnerAngebotsgeber_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("person.person_sqlid", ondelete="SET NULL"))
    )
    unterzeichnerAngebotsgeber: "Person" = Relationship(
        back_populates="angebot_unterzeichnerAngebotsgeber",
        sa_relationship_kwargs={"foreign_keys": "[Angebot.unterzeichnerAngebotsgeber_id]"},
    )
    unterzeichnerAngebotsnehmer_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("person.person_sqlid", ondelete="SET NULL"))
    )
    unterzeichnerAngebotsnehmer: "Person" = Relationship(
        back_populates="angebot_unterzeichnerAngebotsnehmer",
        sa_relationship_kwargs={"foreign_keys": "[Angebot.unterzeichnerAngebotsnehmer_id]"},
    )
    varianten: List["Angebotsvariante"] = Relationship(
        back_populates="angebot_varianten_link", link_model=AngebotvariantenLink
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="angebot_zusatzattribute_link",
        link_model=AngebotzusatzAttributeLink,
    )
