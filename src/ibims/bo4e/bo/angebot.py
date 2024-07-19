from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..com.angebotsvariante import Angebotsvariante
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .geschaeftspartner import Geschaeftspartner
from .person import Person


class Angebot(BaseModel):
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

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.ANGEBOT, alias="_typ")
    """
    Eindeutige Nummer des Angebotes
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
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
    angebotsgeber: Geschaeftspartner | None = None
    """
    Ersteller des Angebots
    """
    angebotsnehmer: Geschaeftspartner | None = None
    """
    Empfänger des Angebots
    """
    angebotsnummer: str | None = Field(default=None, title="Angebotsnummer")
    """
    Eindeutige Nummer des Angebotes
    """
    bindefrist: datetime | None = Field(default=None, title="Bindefrist")
    """
    Bis zu diesem Zeitpunkt (Tag/Uhrzeit) inklusive gilt das Angebot
    """
    sparte: Sparte | None = None
    """
    Sparte, für die das Angebot abgegeben wird (Strom/Gas)
    """
    unterzeichner_angebotsgeber: Person | None = Field(default=None, alias="unterzeichnerAngebotsgeber")
    """
    Person, die als Angebotsgeber das Angebots ausgestellt hat
    """
    unterzeichner_angebotsnehmer: Person | None = Field(default=None, alias="unterzeichnerAngebotsnehmer")
    """
    Person, die als Angebotsnehmer das Angebot angenommen hat
    """
    varianten: list[Angebotsvariante] | None = Field(default=None, title="Varianten")
    """
    Eine oder mehrere Varianten des Angebots mit den Angebotsteilen;
    Ein Angebot besteht mindestens aus einer Variante.
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
