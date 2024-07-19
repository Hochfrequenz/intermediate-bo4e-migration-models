from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..com.adresse import Adresse
from ..com.kontaktweg import Kontaktweg
from ..com.zustaendigkeit import Zustaendigkeit
from ..enum.anrede import Anrede
from ..enum.titel import Titel
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut


class Person(BaseModel):
    """
    Object containing information about a Person

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Person.svg" type="image/svg+xml"></object>

    .. HINT::
        `Person JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Person.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.PERSON, alias="_typ")
    """
    Mögliche Anrede der Person
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    adresse: Adresse | None = None
    """
    Adresse der Person, falls diese von der Adresse des Geschäftspartners abweicht
    """
    anrede: Anrede | None = None
    """
    Mögliche Anrede der Person
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
    kontaktwege: list[Kontaktweg] | None = Field(default=None, title="Kontaktwege")
    """
    Kontaktwege der Person
    """
    nachname: str | None = Field(default=None, title="Nachname")
    """
    Nachname (Familienname) der Person
    """
    titel: Titel | None = None
    """
    Möglicher Titel der Person
    """
    vorname: str | None = Field(default=None, title="Vorname")
    """
    Vorname der Person
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    zustaendigkeiten: list[Zustaendigkeit] | None = Field(default=None, title="Zustaendigkeiten")
    """
    Liste der Abteilungen und Zuständigkeiten der Person
    """
