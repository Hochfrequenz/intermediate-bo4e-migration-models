from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..com.adresse import Adresse
from ..com.kontaktweg import Kontaktweg
from ..enum.anrede import Anrede
from ..enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from ..enum.organisationstyp import Organisationstyp
from ..enum.titel import Titel
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .person import Person


class Geschaeftspartner(BaseModel):
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

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.GESCHAEFTSPARTNER, alias="_typ")
    """
    Mögliche Anrede der Person
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    adresse: Adresse | None = None
    """
    Adresse des Geschäftspartners
    """
    amtsgericht: str | None = Field(default=None, title="Amtsgericht")
    """
    Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat
    """
    anrede: Anrede | None = None
    """
    Mögliche Anrede der Person
    """
    ansprechpartner: list[Person] | None = Field(default=None, title="Ansprechpartner")
    geschaeftspartnerrollen: list[Geschaeftspartnerrolle] | None = Field(default=None, title="Geschaeftspartnerrollen")
    """
    Rollen, die die Geschäftspartner inne haben (z.B. Interessent, Kunde)
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
    kontaktwege: list[Kontaktweg] | None = Field(default=None, title="Kontaktwege")
    """
    Kontaktwege des Geschäftspartners
    """
    nachname: str | None = Field(default=None, title="Nachname")
    """
    Nachname (Familienname) der Person
    """
    organisationsname: str | None = Field(default=None, title="Organisationsname")
    """
    Kontaktwege des Geschäftspartners
    """
    organisationstyp: Organisationstyp | None = None
    """
    organisationsname: Optional[str] = None
    """
    titel: Titel | None = None
    """
    Möglicher Titel der Person
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
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    erstellungsdatum: datetime | None = Field(default=None, title="Erstellungsdatum")
    geburtstag: datetime | None = Field(default=None, title="Geburtstag")
    telefonnummer_mobil: str | None = Field(default=None, alias="telefonnummerMobil", title="Telefonnummermobil")
    telefonnummer_privat: str | None = Field(default=None, alias="telefonnummerPrivat", title="Telefonnummerprivat")
    telefonnummer_geschaeft: str | None = Field(
        default=None, alias="telefonnummerGeschaeft", title="Telefonnummergeschaeft"
    )
    firmenname: str | None = Field(default=None, title="Firmenname")
    hausbesitzer: bool | None = Field(default=None, title="Hausbesitzer")
