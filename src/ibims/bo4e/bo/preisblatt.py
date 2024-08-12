from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enum.preisstatus import Preisstatus
from ..enum.sparte import Sparte
from ..enum.typ import Typ

if TYPE_CHECKING:
    from ..com.preisposition import Preisposition
    from ..com.zeitraum import Zeitraum
    from ..zusatz_attribut import ZusatzAttribut
    from .marktteilnehmer import Marktteilnehmer


class Preisblatt(BaseModel):
    """
    Das allgemeine Modell zur Abbildung von Preisen;
    Davon abgeleitet kÃ¶nnen, Ã¼ber die Zuordnung identifizierender Merkmale, spezielle Preisblatt-Varianten modelliert
    werden.

    Die jeweiligen SÃ¤tze von Merkmalen sind in der Grafik ergÃ¤nzt worden und stellen jeweils eine AusprÃ¤gung fÃ¼r die
    verschiedenen AnwendungsfÃ¤lle der PreisblÃ¤tter dar.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Preisblatt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/bo/Preisblatt.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: Optional[str] = Field(default=None, alias="_id", title=" Id")
    """
    Hier kÃ¶nnen IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.PREISBLATT, alias="_typ")
    """
    Eine Bezeichnung fÃ¼r das Preisblatt
    """
    version: str = Field(default="v202401.4.0", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    bezeichnung: str = Field(..., title="Bezeichnung")
    """
    Eine Bezeichnung fÃ¼r das Preisblatt
    """
    gueltigkeit: "Zeitraum"
    """
    Der Zeitraum fÃ¼r den der Preis festgelegt ist
    """
    herausgeber: Optional["Marktteilnehmer"] = None
    """
    Der Netzbetreiber, der die Preise verÃ¶ffentlicht hat
    """
    preispositionen: list["Preisposition"] = Field(..., title="Preispositionen")
    """
    Die einzelnen Positionen, die mit dem Preisblatt abgerechnet werden kÃ¶nnen. Z.B. Arbeitspreis, Grundpreis etc
    """
    preisstatus: Optional[Preisstatus] = None
    """
    Merkmal, das anzeigt, ob es sich um vorlÃ¤ufige oder endgÃ¼ltige Preise handelt
    """
    sparte: Optional[Sparte] = None
    """
    Preisblatt gilt fÃ¼r angegebene Sparte
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
