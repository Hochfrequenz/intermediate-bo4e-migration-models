from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

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
        `Fremdkostenposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Fremdkostenposition.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = None

    # pylint: disable=duplicate-code
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        extra="allow",
        # json_encoders is deprecated, but there is no easy-to-use alternative. The best way would be to create
        # an annotated version of Decimal, but you would have to use it everywhere in the pydantic models.
        # See this issue for more info: https://github.com/pydantic/pydantic/issues/6375
        json_encoders={Decimal: str},
    )
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    artikelbezeichnung: str | None = Field(default=None, title="Artikelbezeichnung")
    """
    Bezeichnung für den Artikel für den die Kosten ermittelt wurden. Beispiel: Arbeitspreis HT
    """
    artikeldetail: str | None = Field(default=None, title="Artikeldetail")
    """
    Detaillierung des Artikels (optional). Beispiel: 'Drehstromzähler'
    """
    betrag_kostenposition: Betrag | None = Field(default=None, alias="betragKostenposition")
    """
    Der errechnete Gesamtbetrag der Position als Ergebnis der Berechnung <Menge * Einzelpreis> oder
    <Einzelpreis / (Anzahl Tage Jahr) * zeitmenge>
    """
    bis: datetime | None = Field(default=None, title="Bis")
    """
    exklusiver bis-Zeitpunkt der Kostenzeitscheibe
    """
    einzelpreis: Preis | None = None
    """
    Der Preis für eine Einheit. Beispiele: 5,8200 ct/kWh oder 55 €/Jahr.
    """
    gebietcode_eic: str | None = Field(default=None, alias="gebietcodeEic", title="Gebietcodeeic")
    """
    EIC-Code des Regel- oder Marktgebietes eingetragen. Z.B. '10YDE-EON------1' für die Regelzone TenneT
    """
    link_preisblatt: str | None = Field(default=None, alias="linkPreisblatt", title="Linkpreisblatt")
    """
    Link zum veröffentlichten Preisblatt
    """
    marktpartnercode: str | None = Field(default=None, title="Marktpartnercode")
    """
    Die Codenummer (z.B. BDEW-Codenummer) des Marktpartners, der die Preise festlegt / die Kosten in Rechnung stellt
    """
    marktpartnername: str | None = Field(default=None, title="Marktpartnername")
    """
    Der Name des Marktpartners, der die Preise festlegt, bzw. die Kosten in Rechnung stellt
    """
    menge: Menge | None = None
    """
    Die Menge, die in die Kostenberechnung eingeflossen ist. Beispiel: 3.660 kWh
    """
    positionstitel: str | None = Field(default=None, title="Positionstitel")
    """
    Ein Titel für die Zeile. Hier kann z.B. der Netzbetreiber eingetragen werden, wenn es sich um Netzkosten handelt.
    """
    von: datetime | None = Field(default=None, title="Von")
    """
    inklusiver von-Zeitpunkt der Kostenzeitscheibe
    """
    zeitmenge: Menge | None = None
    """
    Detaillierung des Artikels (optional). Beispiel: 'Drehstromzähler'
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
