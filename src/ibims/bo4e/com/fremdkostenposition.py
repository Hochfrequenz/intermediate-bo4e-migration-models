from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..zusatz_attribut import ZusatzAttribut
    from .betrag import Betrag
    from .menge import Menge
    from .preis import Preis


class Fremdkostenposition(BaseModel):
    """
    Eine Kostenposition im Bereich der Fremdkosten

    .. raw:: html

        <object data="../_static/images/bo4e/com/Fremdkostenposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Fremdkostenposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/com/Fremdkostenposition.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: Optional[str] = Field(default=None, alias="_id", title=" Id")
    """
    Eine generische ID, die fÃ¼r eigene Zwecke genutzt werden kann.
    Z.B. kÃ¶nnten hier UUIDs aus einer Datenbank stehen oder URLs zu einem Backend-System.
    """
    version: str = Field(default="v202401.4.0", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    artikelbezeichnung: Optional[str] = Field(default=None, title="Artikelbezeichnung")
    """
    Bezeichnung fÃ¼r den Artikel fÃ¼r den die Kosten ermittelt wurden. Beispiel: Arbeitspreis HT
    """
    artikeldetail: Optional[str] = Field(default=None, title="Artikeldetail")
    """
    Detaillierung des Artikels (optional). Beispiel: 'DrehstromzÃ¤hler'
    """
    betrag_kostenposition: Optional["Betrag"] = Field(default=None, alias="betragKostenposition")
    """
    Der errechnete Gesamtbetrag der Position als Ergebnis der Berechnung <Menge * Einzelpreis> oder
    <Einzelpreis / (Anzahl Tage Jahr) * zeitmenge>
    """
    bis: Optional[datetime] = Field(default=None, title="Bis")
    """
    exklusiver bis-Zeitpunkt der Kostenzeitscheibe
    """
    einzelpreis: Optional["Preis"] = None
    """
    Der Preis fÃ¼r eine Einheit. Beispiele: 5,8200 ct/kWh oder 55 â‚¬/Jahr.
    """
    gebietcode_eic: Optional[str] = Field(default=None, alias="gebietcodeEic", title="Gebietcodeeic")
    """
    EIC-Code des Regel- oder Marktgebietes eingetragen. Z.B. '10YDE-EON------1' fÃ¼r die Regelzone TenneT
    """
    link_preisblatt: Optional[str] = Field(default=None, alias="linkPreisblatt", title="Linkpreisblatt")
    """
    Link zum verÃ¶ffentlichten Preisblatt
    """
    marktpartnercode: Optional[str] = Field(default=None, title="Marktpartnercode")
    """
    Die Codenummer (z.B. BDEW-Codenummer) des Marktpartners, der die Preise festlegt / die Kosten in Rechnung stellt
    """
    marktpartnername: Optional[str] = Field(default=None, title="Marktpartnername")
    """
    Der Name des Marktpartners, der die Preise festlegt, bzw. die Kosten in Rechnung stellt
    """
    menge: Optional["Menge"] = None
    """
    Die Menge, die in die Kostenberechnung eingeflossen ist. Beispiel: 3.660 kWh
    """
    positionstitel: Optional[str] = Field(default=None, title="Positionstitel")
    """
    Ein Titel fÃ¼r die Zeile. Hier kann z.B. der Netzbetreiber eingetragen werden, wenn es sich um Netzkosten handelt.
    """
    von: Optional[datetime] = Field(default=None, title="Von")
    """
    inklusiver von-Zeitpunkt der Kostenzeitscheibe
    """
    zeitmenge: Optional["Menge"] = None
    """
    Wenn es einen zeitbasierten Preis gibt (z.B. â‚¬/Jahr), dann ist hier die Menge angegeben mit der die Kosten berechnet
    wurden. Z.B. 138 Tage.
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
