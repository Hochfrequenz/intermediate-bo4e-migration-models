from pydantic import BaseModel, ConfigDict, Field

from ..com.preisposition import Preisposition
from ..com.zeitraum import Zeitraum
from ..enum.preisstatus import Preisstatus
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .marktteilnehmer import Marktteilnehmer


class Preisblatt(BaseModel):
    """
    Das allgemeine Modell zur Abbildung von Preisen;
    Davon abgeleitet können, über die Zuordnung identifizierender Merkmale, spezielle Preisblatt-Varianten modelliert
    werden.

    Die jeweiligen Sätze von Merkmalen sind in der Grafik ergänzt worden und stellen jeweils eine Ausprägung für die
    verschiedenen Anwendungsfälle der Preisblätter dar.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Preisblatt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Preisblatt.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.PREISBLATT, alias="_typ")
    """
    Eine Bezeichnung für das Preisblatt
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    bezeichnung: str = Field(..., title="Bezeichnung")
    """
    Eine Bezeichnung für das Preisblatt
    """
    gueltigkeit: Zeitraum
    """
    Der Zeitraum für den der Preis festgelegt ist
    """
    herausgeber: Marktteilnehmer | None = None
    """
    Der Netzbetreiber, der die Preise veröffentlicht hat
    """
    preispositionen: list[Preisposition] = Field(..., title="Preispositionen")
    """
    Die einzelnen Positionen, die mit dem Preisblatt abgerechnet werden können. Z.B. Arbeitspreis, Grundpreis etc
    """
    preisstatus: Preisstatus | None = None
    """
    Merkmal, das anzeigt, ob es sich um vorläufige oder endgültige Preise handelt
    """
    sparte: Sparte | None = None
    """
    Preisblatt gilt für angegebene Sparte
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
