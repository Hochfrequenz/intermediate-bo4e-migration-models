from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..com.betrag import Betrag
from ..com.rechnungsposition import Rechnungsposition
from ..com.steuerbetrag import Steuerbetrag
from ..com.zeitraum import Zeitraum
from ..enum.netznutzung_rechnungsart import NetznutzungRechnungsart
from ..enum.netznutzung_rechnungstyp import NetznutzungRechnungstyp
from ..enum.rechnungsstatus import Rechnungsstatus
from ..enum.rechnungstyp import Rechnungstyp
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .geschaeftspartner import Geschaeftspartner
from .marktlokation import Marktlokation
from .messlokation import Messlokation


class Rechnung(BaseModel):
    """
    Modell für die Abbildung von Rechnungen und Netznutzungsrechnungen im Kontext der Energiewirtschaft;

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Rechnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rechnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Rechnung.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.RECHNUNG, alias="_typ")
    """
    Der Zeitraum der zugrunde liegenden Lieferung zur Rechnung
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    faelligkeitsdatum: datetime | None = Field(default=None, title="Faelligkeitsdatum")
    """
    Zu diesem Datum ist die Zahlung fällig
    """
    gesamtbrutto: Betrag
    """
    Die Summe aus Netto- und Steuerbetrag
    """
    gesamtnetto: Betrag | None = None
    """
    Die Summe der Nettobeträge der Rechnungsteile
    """
    gesamtsteuer: Betrag
    """
    Die Summe der Steuerbeträge der Rechnungsteile
    """
    ist_original: bool | None = Field(default=None, alias="istOriginal", title="Istoriginal")
    """
    Kennzeichen, ob es sich um ein Original (true) oder eine Kopie handelt (false)
    """
    ist_simuliert: bool | None = Field(default=None, alias="istSimuliert", title="Istsimuliert")
    """
    Kennzeichen, ob es sich um eine simulierte Rechnung, z.B. zur Rechnungsprüfung handelt
    """
    ist_storno: bool | None = Field(default=None, alias="istStorno", title="Iststorno")
    """
    Eine im Verwendungskontext eindeutige Nummer für die Rechnung
    """
    marktlokation: Marktlokation | None = None
    """
    Marktlokation, auf die sich die Rechnung bezieht
    """
    messlokation: Messlokation | None = None
    """
    Messlokation, auf die sich die Rechnung bezieht
    """
    netznutzungrechnungsart: NetznutzungRechnungsart | None = None
    """
    Aus der INVOIC entnommen, befüllt wenn es sich um eine Netznutzungsrechnung handelt
    """
    netznutzungrechnungstyp: NetznutzungRechnungstyp | None = None
    """
    Aus der INVOIC entnommen, befüllt wenn es sich um eine Netznutzungsrechnung handelt
    """
    original_rechnungsnummer: str | None = Field(
        default=None, alias="originalRechnungsnummer", title="Originalrechnungsnummer"
    )
    """
    Im Falle einer Stornorechnung (storno = true) steht hier die Rechnungsnummer der stornierten Rechnung
    """
    rabatt_brutto: Betrag | None = Field(default=None, alias="rabattBrutto")
    """
    Gesamtrabatt auf den Bruttobetrag
    """
    rechnungsdatum: datetime | None = Field(default=None, title="Rechnungsdatum")
    """
    Ausstellungsdatum der Rechnung
    """
    rechnungsempfaenger: Geschaeftspartner | None = None
    """
    Der Aussteller der Rechnung, die Rollencodenummer kennt man über den im Geschäftspartner verlinkten Marktteilnehmer
    """
    rechnungsersteller: Geschaeftspartner | None = None
    """
    Der Aussteller der Rechnung, die Rollencodenummer kennt man über den im Geschäftspartner verlinkten Marktteilnehmer
    """
    rechnungsnummer: str | None = Field(default=None, title="Rechnungsnummer")
    """
    Eine im Verwendungskontext eindeutige Nummer für die Rechnung
    """
    rechnungsperiode: Zeitraum | None = None
    """
    Der Zeitraum der zugrunde liegenden Lieferung zur Rechnung
    """
    rechnungspositionen: list[Rechnungsposition] | None = Field(default=None, title="Rechnungspositionen")
    """
    Die Rechnungspositionen
    """
    rechnungsstatus: Rechnungsstatus | None = None
    """
    Status der Rechnung zur Kennzeichnung des Bearbeitungsstandes
    """
    rechnungstitel: str | None = Field(default=None, title="Rechnungstitel")
    """
    Bezeichnung für die vorliegende Rechnung
    """
    rechnungstyp: Rechnungstyp
    """
    Ein kontextbezogender Rechnungstyp, z.B. Netznutzungsrechnung
    """
    sparte: Sparte | None = None
    """
    Sparte (Strom, Gas ...) für die die Rechnung ausgestellt ist
    """
    steuerbetraege: list[Steuerbetrag] | None = Field(default=None, title="Steuerbetraege")
    """
    Sparte (Strom, Gas ...) für die die Rechnung ausgestellt ist
    """
    vorausgezahlt: Betrag | None = None
    """
    Die Summe evtl. vorausgezahlter Beträge, z.B. Abschläge. Angabe als Bruttowert
    """
    zu_zahlen: Betrag | None = Field(default=None, alias="zuZahlen")
    """
    Der zu zahlende Betrag, der sich aus (gesamtbrutto - vorausbezahlt - rabattBrutto) ergibt
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    ist_selbstausgestellt: bool | None = Field(default=None, alias="istSelbstausgestellt", title="Istselbstausgestellt")
    ist_reverse_charge: bool | None = Field(default=None, alias="istReverseCharge", title="Istreversecharge")
