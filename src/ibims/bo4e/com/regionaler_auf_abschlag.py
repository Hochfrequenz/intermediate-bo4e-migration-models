from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enum.auf_abschlagstyp import AufAbschlagstyp
from ..enum.auf_abschlagsziel import AufAbschlagsziel
from ..enum.waehrungseinheit import Waehrungseinheit

if TYPE_CHECKING:
    from ..zusatz_attribut import ZusatzAttribut
    from .energiemix import Energiemix
    from .preisgarantie import Preisgarantie
    from .regionale_preisstaffel import RegionalePreisstaffel
    from .tarifeinschraenkung import Tarifeinschraenkung
    from .vertragskonditionen import Vertragskonditionen
    from .zeitraum import Zeitraum


class RegionalerAufAbschlag(BaseModel):
    """
    Mit dieser Komponente kÃ¶nnen Auf- und AbschlÃ¤ge verschiedener Typen im Zusammenhang mit regionalen GÃ¼ltigkeiten
    abgebildet werden.
    Hier sind auch die Auswirkungen auf verschiedene Tarifparameter modelliert, die sich durch die Auswahl eines Auf-
    oder Abschlags ergeben.

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalerAufAbschlag.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalerAufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/com/RegionalerAufAbschlag.json>`_
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
    auf_abschlagstyp: Optional[AufAbschlagstyp] = Field(default=None, alias="aufAbschlagstyp")
    """
    Typ des Aufabschlages (z.B. absolut oder prozentual)
    """
    auf_abschlagsziel: Optional[AufAbschlagsziel] = Field(default=None, alias="aufAbschlagsziel")
    """
    Diesem Preis oder den Kosten ist der Auf/Abschlag zugeordnet. Z.B. Arbeitspreis, Gesamtpreis etc.
    """
    beschreibung: Optional[str] = Field(default=None, title="Beschreibung")
    """
    Beschreibung des Auf-/Abschlags
    """
    bezeichnung: Optional[str] = Field(default=None, title="Bezeichnung")
    """
    Bezeichnung des Auf-/Abschlags
    """
    einheit: Optional[Waehrungseinheit] = None
    """
    Gibt an in welcher WÃ¤hrungseinheit der Auf/Abschlag berechnet wird (nur im Falle absoluter Aufschlagstypen).
    """
    einschraenkungsaenderung: Optional["Tarifeinschraenkung"] = None
    """
    Ã„nderungen in den EinschrÃ¤nkungen zum Tarif;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit Ã¼berschrieben.
    """
    energiemixaenderung: Optional["Energiemix"] = None
    """
    Der Energiemix kann sich durch einen AufAbschlag Ã¤ndern (z.B. zwei Cent Aufschlag fÃ¼r Ã–kostrom).
    Sollte dies der Fall sein, wird hier die neue Zusammensetzung des Energiemix angegeben.
    """
    garantieaenderung: Optional["Preisgarantie"] = None
    """
    Ã„nderungen in den Garantievereinbarungen;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit Ã¼berschrieben.
    """
    gueltigkeitszeitraum: Optional["Zeitraum"] = None
    """
    Zeitraum, in dem der Abschlag zur Anwendung kommen kann
    """
    staffeln: Optional[list["RegionalePreisstaffel"]] = Field(default=None, title="Staffeln")
    """
    Werte fÃ¼r die gestaffelten Auf/AbschlÃ¤ge mit regionaler Eingrenzung
    """
    tarifnamensaenderungen: Optional[str] = Field(default=None, title="Tarifnamensaenderungen")
    """
    Durch die Anwendung des Auf/Abschlags kann eine Ã„nderung des Tarifnamens auftreten
    """
    vertagskonditionsaenderung: Optional["Vertragskonditionen"] = None
    """
    Ã„nderungen in den Vertragskonditionen;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit Ã¼berschrieben.
    """
    voraussetzungen: Optional[list[str]] = Field(default=None, title="Voraussetzungen")
    """
    Voraussetzungen, die erfÃ¼llt sein mÃ¼ssen, damit dieser AufAbschlag zur Anwendung kommen kann
    """
    website: Optional[str] = Field(default=None, title="Website")
    """
    Internetseite, auf der die Informationen zum Auf-/Abschlag verÃ¶ffentlicht sind
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    zusatzprodukte: Optional[list[str]] = Field(default=None, title="Zusatzprodukte")
    """
    Zusatzprodukte, die nur in Kombination mit diesem AufAbschlag erhÃ¤ltlich sind
    """
