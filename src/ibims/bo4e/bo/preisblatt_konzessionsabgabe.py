from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enum.kundengruppe_ka import KundengruppeKA
from ..enum.preisstatus import Preisstatus
from ..enum.sparte import Sparte
from ..enum.typ import Typ

if TYPE_CHECKING:
    from ..com.preisposition import Preisposition
    from ..com.zeitraum import Zeitraum
    from ..zusatz_attribut import ZusatzAttribut
    from .marktteilnehmer import Marktteilnehmer


class PreisblattKonzessionsabgabe(BaseModel):
    """
    Die Variante des Preisblattmodells zur Abbildung von allgemeinen Abgaben

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattKonzessionsabgabe.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattKonzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/bo/PreisblattKonzessionsabgabe.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: Optional[str] = Field(default=None, alias="_id", title=" Id")
    """
    Hier kÃ¶nnen IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.PREISBLATTKONZESSIONSABGABE, alias="_typ")
    """
    Kundegruppe anhand derer die HÃ¶he der Konzessionabgabe festgelegt ist
    """
    version: str = Field(default="v202401.4.0", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    bezeichnung: Optional[str] = Field(default=None, title="Bezeichnung")
    """
    Eine Bezeichnung fÃ¼r das Preisblatt
    """
    gueltigkeit: Optional["Zeitraum"] = None
    """
    Der Zeitraum fÃ¼r den der Preis festgelegt ist
    """
    herausgeber: Optional["Marktteilnehmer"] = None
    """
    Der Netzbetreiber, der die Preise verÃ¶ffentlicht hat
    """
    kundengruppe_ka: Optional[KundengruppeKA] = Field(default=None, alias="kundengruppeKA")
    """
    Kundegruppe anhand derer die HÃ¶he der Konzessionabgabe festgelegt ist
    """
    preispositionen: Optional[list["Preisposition"]] = Field(default=None, title="Preispositionen")
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
