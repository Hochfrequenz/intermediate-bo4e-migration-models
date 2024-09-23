import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import ARRAY, Column, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.anrede import Anrede
from ibims.orm.models.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from ibims.orm.models.enum.organisationstyp import Organisationstyp
from ibims.orm.models.enum.titel import Titel
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.many import (
    GeschaeftspartneransprechpartnerLink,
    GeschaeftspartnerkontaktwegeLink,
    GeschaeftspartnerzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.angebot import Angebot
    from ibims.orm.models.bo.ausschreibung import Ausschreibung
    from ibims.orm.models.bo.buendelvertrag import Buendelvertrag
    from ibims.orm.models.bo.marktlokation import Marktlokation
    from ibims.orm.models.bo.marktteilnehmer import Marktteilnehmer
    from ibims.orm.models.bo.person import Person
    from ibims.orm.models.bo.rechnung import Rechnung
    from ibims.orm.models.bo.vertrag import Vertrag
    from ibims.orm.models.bo.zaehler import Zaehler
    from ibims.orm.models.bo.zaehler_gas import ZaehlerGas
    from ibims.orm.models.com.adresse import Adresse
    from ibims.orm.models.com.kontaktweg import Kontaktweg
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Geschaeftspartner(SQLModel, table=True):
    """
    Mit diesem Objekt können Geschäftspartner übertragen werden.
    Sowohl Unternehmen, als auch Privatpersonen können Geschäftspartner sein.
    Hinweis: "Marktteilnehmer" haben ein eigenes BO, welches sich von diesem BO ableitet.
    Hier sollte daher keine Zuordnung zu Marktrollen erfolgen.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geschaeftspartner.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geschaeftspartner JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Geschaeftspartner.json>`_
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
    amtsgericht: str | None = Field(default=None, title="Amtsgericht")
    """
    Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat
    """
    glaeubiger_id: str | None = Field(default=None, alias="glaeubigerId", title="Glaeubigerid")
    """
    Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird; Z.B. "DE 47116789"
    """
    handelsregisternummer: str | None = Field(default=None, title="Handelsregisternummer")
    """
    Handelsregisternummer des Geschäftspartners
    """
    individuelle_anrede: str | None = Field(default=None, alias="individuelleAnrede", title="Individuelleanrede")
    """
    Im Falle einer nicht standardisierten Anrede kann hier eine frei definierbare Anrede vorgegeben werden.
    Beispiel: "Vereinsgemeinschaft", "Pfarrer", "Hochwürdigster Herr Abt".
    """
    nachname: str | None = Field(default=None, title="Nachname")
    """
    Nachname (Familienname) der Person
    """
    organisationsname: str | None = Field(default=None, title="Organisationsname")
    """
    Kontaktwege des Geschäftspartners
    """
    umsatzsteuer_id: str | None = Field(default=None, alias="umsatzsteuerId", title="Umsatzsteuerid")
    """
    Die Steuer-ID des Geschäftspartners; Beispiel: "DE 813281825"
    """
    vorname: str | None = Field(default=None, title="Vorname")
    """
    Vorname der Person
    """
    website: str | None = Field(default=None, title="Website")
    """
    Internetseite des Marktpartners
    """
    erstellungsdatum: datetime | None = Field(default=None, title="Erstellungsdatum")
    geburtstag: datetime | None = Field(default=None, title="Geburtstag")
    telefonnummer_mobil: str | None = Field(default=None, alias="telefonnummerMobil", title="Telefonnummermobil")
    telefonnummer_privat: str | None = Field(default=None, alias="telefonnummerPrivat", title="Telefonnummerprivat")
    telefonnummer_geschaeft: str | None = Field(
        default=None, alias="telefonnummerGeschaeft", title="Telefonnummergeschaeft"
    )
    firmenname: str | None = Field(default=None, title="Firmenname")
    hausbesitzer: bool | None = Field(default=None, title="Hausbesitzer")
    geschaeftspartner_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    angebot_angebotsgeber: List["Angebot"] = Relationship(
        back_populates="angebotsgeber",
        sa_relationship_kwargs={
            "primaryjoin": "Angebot.angebotsgeber_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    angebot_angebotsnehmer: List["Angebot"] = Relationship(
        back_populates="angebotsnehmer",
        sa_relationship_kwargs={
            "primaryjoin": "Angebot.angebotsnehmer_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibung_ausschreibender: List["Ausschreibung"] = Relationship(
        back_populates="ausschreibender",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibung.ausschreibender_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    buendelvertrag_vertragspartner1: List["Buendelvertrag"] = Relationship(
        back_populates="vertragspartner1",
        sa_relationship_kwargs={
            "primaryjoin": "Buendelvertrag.vertragspartner1_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    buendelvertrag_vertragspartner2: List["Buendelvertrag"] = Relationship(
        back_populates="vertragspartner2",
        sa_relationship_kwargs={
            "primaryjoin": "Buendelvertrag.vertragspartner2_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    typ: Typ | None = Field(Typ.GESCHAEFTSPARTNER)
    adresse_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("adresse.adresse_sqlid", ondelete="SET NULL"))
    )
    adresse: "Adresse" = Relationship(
        back_populates="geschaeftspartner_adresse",
        sa_relationship_kwargs={"foreign_keys": "[Geschaeftspartner.adresse_id]"},
    )
    anrede: Anrede | None = Field(None)
    ansprechpartner: List["Person"] = Relationship(
        back_populates="geschaeftspartner_ansprechpartner_link",
        link_model=GeschaeftspartneransprechpartnerLink,
    )
    geschaeftspartnerrollen: List[Geschaeftspartnerrolle] | None = Field(
        None,
        sa_column=Column(ARRAY(Enum(Geschaeftspartnerrolle, name="geschaeftspartnerrolle"))),
    )
    kontaktwege: List["Kontaktweg"] = Relationship(
        back_populates="geschaeftspartner_kontaktwege_link",
        link_model=GeschaeftspartnerkontaktwegeLink,
    )
    organisationstyp: Organisationstyp | None = Field(None)
    titel: Titel | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="geschaeftspartner_zusatzattribute_link",
        link_model=GeschaeftspartnerzusatzAttributeLink,
    )
    marktlokation_endkunde: List["Marktlokation"] = Relationship(
        back_populates="endkunde",
        sa_relationship_kwargs={
            "primaryjoin": "Marktlokation.endkunde_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    marktteilnehmer_geschaeftspartner: List["Marktteilnehmer"] = Relationship(
        back_populates="geschaeftspartner",
        sa_relationship_kwargs={
            "primaryjoin": "Marktteilnehmer.geschaeftspartner_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    rechnung_rechnungsempfaenger: List["Rechnung"] = Relationship(
        back_populates="rechnungsempfaenger",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnung.rechnungsempfaenger_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    rechnung_rechnungsersteller: List["Rechnung"] = Relationship(
        back_populates="rechnungsersteller",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnung.rechnungsersteller_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    vertrag_vertragspartner1: List["Vertrag"] = Relationship(
        back_populates="vertragspartner1",
        sa_relationship_kwargs={
            "primaryjoin": "Vertrag.vertragspartner1_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    vertrag_vertragspartner2: List["Vertrag"] = Relationship(
        back_populates="vertragspartner2",
        sa_relationship_kwargs={
            "primaryjoin": "Vertrag.vertragspartner2_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    zaehler_zaehlerhersteller: List["Zaehler"] = Relationship(
        back_populates="zaehlerhersteller",
        sa_relationship_kwargs={
            "primaryjoin": "Zaehler.zaehlerhersteller_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
    zaehlergas_zaehlerhersteller: List["ZaehlerGas"] = Relationship(
        back_populates="zaehlerhersteller",
        sa_relationship_kwargs={
            "primaryjoin": "ZaehlerGas.zaehlerhersteller_id==Geschaeftspartner.geschaeftspartner_sqlid",
            "lazy": "joined",
        },
    )
