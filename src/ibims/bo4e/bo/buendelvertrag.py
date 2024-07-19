from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..com.unterschrift import Unterschrift
from ..com.vertragskonditionen import Vertragskonditionen
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..enum.vertragsart import Vertragsart
from ..enum.vertragsstatus import Vertragsstatus
from ..zusatz_attribut import ZusatzAttribut
from .geschaeftspartner import Geschaeftspartner
from .vertrag import Vertrag


class Buendelvertrag(BaseModel):
    """
    Abbildung eines Bündelvertrags.
    Es handelt sich hierbei um eine Liste von Einzelverträgen, die in einem Vertragsobjekt gebündelt sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Buendelvertrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Buendelvertrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Buendelvertrag.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.BUENDELVERTRAG, alias="_typ")
    """
    Der Typ des Geschäftsobjektes
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    """
    Beschreibung zum Vertrag
    """
    einzelvertraege: list[Vertrag] | None = Field(default=None, title="Einzelvertraege")
    """
    Die Liste mit den Einzelverträgen zu den Abnahmestellen
    """
    sparte: Sparte | None = None
    """
    Unterscheidungsmöglichkeiten für die Sparte
    """
    unterzeichnervp1: list[Unterschrift] | None = Field(default=None, title="Unterzeichnervp1")
    """
    Unterzeichner des Vertragspartners1
    """
    unterzeichnervp2: list[Unterschrift] | None = Field(default=None, title="Unterzeichnervp2")
    """
    Unterzeichner des Vertragspartners2
    """
    vertragsart: Vertragsart | None = None
    """
    Hier ist festgelegt, um welche Art von Vertrag es sich handelt. Z.B. Netznutzungvertrag
    """
    vertragsbeginn: datetime | None = Field(default=None, title="Vertragsbeginn")
    """
    Gibt an, wann der Vertrag beginnt (inklusiv)
    """
    vertragsende: datetime | None = Field(default=None, title="Vertragsende")
    """
    Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde (exklusiv)
    """
    vertragskonditionen: list[Vertragskonditionen] | None = Field(default=None, title="Vertragskonditionen")
    """
    Festlegungen zu Laufzeiten und Kündigungsfristen
    """
    vertragsnummer: str | None = Field(default=None, title="Vertragsnummer")
    """
    Eine im Verwendungskontext eindeutige Nummer für den Vertrag
    """
    vertragspartner1: Geschaeftspartner | None = None
    """
    Beispiel: "Vertrag zwischen Vertagspartner 1 ..."
    """
    vertragspartner2: Geschaeftspartner | None = None
    """
    Beispiel "Vertrag zwischen Vertagspartner 1 und Vertragspartner 2"
    """
    vertragsstatus: Vertragsstatus | None = None
    """
    Gibt den Status des Vertrages an
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
