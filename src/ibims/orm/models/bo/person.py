import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.anrede import Anrede
from ibims.orm.models.enum.titel import Titel
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import (
    GeschaeftspartneransprechpartnerLink,
    PersonkontaktwegeLink,
    PersonzusatzAttributeLink,
    PersonzustaendigkeitenLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.angebot import Angebot
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.com.adresse import Adresse
    from ibims.orm.models.com.kontaktweg import Kontaktweg
    from ibims.orm.models.com.zustaendigkeit import Zustaendigkeit
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Person(SQLModel, table=True):
    """
    Object containing information about a Person

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Person.svg" type="image/svg+xml"></object>

    .. HINT::
        `Person JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Person.json>`_
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
    geburtsdatum: datetime | None = Field(default=None, title="Geburtsdatum")
    """
    Geburtsdatum der Person
    """
    individuelle_anrede: str | None = Field(default=None, alias="individuelleAnrede", title="Individuelleanrede")
    """
    Im Falle einer nicht standardisierten Anrede kann hier eine frei definierbare Anrede vorgegeben werden.
    Beispiel: "Vereinsgemeinschaft", "Pfarrer", "Hochwürdigster Herr Abt".
    """
    kommentar: str | None = Field(default=None, title="Kommentar")
    """
    Weitere Informationen zur Person
    """
    nachname: str | None = Field(default=None, title="Nachname")
    """
    Nachname (Familienname) der Person
    """
    vorname: str | None = Field(default=None, title="Vorname")
    """
    Vorname der Person
    """
    person_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    angebot_unterzeichnerAngebotsgeber: List["Angebot"] = Relationship(
        back_populates="unterzeichnerAngebotsgeber",
        sa_relationship_kwargs={
            "primaryjoin": "Angebot.unterzeichnerAngebotsgeber_id==Person.person_sqlid",
            "lazy": "joined",
        },
    )
    angebot_unterzeichnerAngebotsnehmer: List["Angebot"] = Relationship(
        back_populates="unterzeichnerAngebotsnehmer",
        sa_relationship_kwargs={
            "primaryjoin": "Angebot.unterzeichnerAngebotsnehmer_id==Person.person_sqlid",
            "lazy": "joined",
        },
    )
    geschaeftspartner_ansprechpartner_link: List["Geschaeftspartner"] = Relationship(
        back_populates="ansprechpartner",
        link_model=GeschaeftspartneransprechpartnerLink,
    )
    typ: Typ | None = Field(Typ.PERSON)
    adresse_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("adresse.adresse_sqlid", ondelete="SET NULL"))
    )
    adresse: "Adresse" = Relationship(
        back_populates="person_adresse",
        sa_relationship_kwargs={"foreign_keys": "[Person.adresse_id]"},
    )
    anrede: Anrede | None = Field(None)
    kontaktwege: List["Kontaktweg"] = Relationship(
        back_populates="person_kontaktwege_link", link_model=PersonkontaktwegeLink
    )
    titel: Titel | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="person_zusatzattribute_link",
        link_model=PersonzusatzAttributeLink,
    )
    zustaendigkeiten: List["Zustaendigkeit"] = Relationship(
        back_populates="person_zustaendigkeiten_link",
        link_model=PersonzustaendigkeitenLink,
    )
