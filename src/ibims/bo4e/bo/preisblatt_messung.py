from pydantic import BaseModel, ConfigDict, Field

from ..com.preisposition import Preisposition
from ..com.zeitraum import Zeitraum
from ..enum.bilanzierungsmethode import Bilanzierungsmethode
from ..enum.dienstleistungstyp import Dienstleistungstyp
from ..enum.netzebene import Netzebene
from ..enum.preisstatus import Preisstatus
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .geraet import Geraet
from .marktteilnehmer import Marktteilnehmer
from .zaehler import Zaehler


class PreisblattMessung(BaseModel):
    """
    Variante des Preisblattmodells zur Abbildung der Preise des Messstellenbetriebs und damit verbundener Leistungen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattMessung.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattMessung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/PreisblattMessung.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.PREISBLATTMESSUNG, alias="_typ")
    """
    Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Eine Bezeichnung für das Preisblatt
    """
    bilanzierungsmethode: Bilanzierungsmethode | None = None
    """
    Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    """
    gueltigkeit: Zeitraum | None = None
    """
    Der Zeitraum für den der Preis festgelegt ist
    """
    herausgeber: Marktteilnehmer | None = None
    """
    Der Netzbetreiber, der die Preise veröffentlicht hat
    """
    inklusive_dienstleistungen: list[Dienstleistungstyp] | None = Field(
        default=None,
        alias="inklusiveDienstleistungen",
        title="Inklusivedienstleistungen",
    )
    """
    Im Preis sind die hier angegebenen Dienstleistungen enthalten, z.B. Jährliche Ablesung
    """
    inklusive_geraete: list[Geraet] | None = Field(default=None, alias="inklusiveGeraete", title="Inklusivegeraete")
    """
    Im Preis sind die hier angegebenen Geräte mit enthalten, z.B. ein Wandler
    """
    messebene: Netzebene | None = None
    """
    Die Preise gelten für Messlokationen in der angebebenen Netzebene
    """
    preispositionen: list[Preisposition] | None = Field(default=None, title="Preispositionen")
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
    zaehler: Zaehler | None = None
    """
    Der Preis betrifft den hier angegebenen Zähler, z.B. einen Drehstromzähler
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
