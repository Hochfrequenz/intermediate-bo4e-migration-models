from pydantic import BaseModel, ConfigDict, Field

from ..enum.auf_abschlagstyp import AufAbschlagstyp
from ..enum.auf_abschlagsziel import AufAbschlagsziel
from ..enum.waehrungseinheit import Waehrungseinheit
from ..zusatz_attribut import ZusatzAttribut
from .auf_abschlag_pro_ort import AufAbschlagProOrt
from .energiemix import Energiemix
from .preisgarantie import Preisgarantie
from .tarifeinschraenkung import Tarifeinschraenkung
from .vertragskonditionen import Vertragskonditionen
from .zeitraum import Zeitraum


class AufAbschlagRegional(BaseModel):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen
    im Zusammenhang mit regionalen Gültigkeiten abgebildet werden.
    Hier sind auch die Auswirkungen auf verschiedene Tarifparameter modelliert,
    die sich durch die Auswahl eines Auf- oder Abschlags ergeben.

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagRegional.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagRegional JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/AufAbschlagRegional.json>`_
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
    auf_abschlagstyp: AufAbschlagstyp | None = Field(default=None, alias="aufAbschlagstyp")
    """
    Typ des Aufabschlages (z.B. absolut oder prozentual)
    """
    auf_abschlagsziel: AufAbschlagsziel | None = Field(default=None, alias="aufAbschlagsziel")
    """
    Diesem Preis oder den Kosten ist der Auf/Abschlag zugeordnet. Z.B. Arbeitspreis, Gesamtpreis etc.
    """
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    """
    Beschreibung zum Auf-/Abschlag
    """
    betraege: list[AufAbschlagProOrt] | None = Field(default=None, title="Betraege")
    """
    Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Bezeichnung des Auf-/Abschlags
    """
    einheit: Waehrungseinheit | None = None
    """
    Gibt an in welcher Währungseinheit der Auf/Abschlag berechnet wird. Euro oder Ct.
    """
    einschraenkungsaenderung: Tarifeinschraenkung | None = None
    """
    Änderungen in den Einschränkungen zum Tarif. Falls in dieser Komponenten angegeben,
    werden die Tarifparameter hiermit überschrieben.
    """
    energiemixaenderung: Energiemix | None = None
    """
    Der Energiemix kann sich durch einen AufAbschlag ändern (z.B. zwei Cent Aufschlag für Ökostrom:
    Sollte dies der Fall sein, wird hier die neue Zusammensetzung des Energiemix angegeben.
    """
    garantieaenderung: Preisgarantie | None = None
    """
    Änderungen in den Garantievereinbarungen. Falls in dieser Komponenten angegeben,
    werden die Tarifparameter hiermit überschrieben.
    """
    gueltigkeitszeitraum: Zeitraum | None = None
    """
    Zeitraum, in dem der Abschlag zur Anwendung kommen kann
    """
    tarifnamensaenderungen: str | None = Field(default=None, title="Tarifnamensaenderungen")
    """
    Durch die Anwendung des Auf/Abschlags kann eine Änderung des Tarifnamens auftreten.
    """
    vertagskonditionsaenderung: Vertragskonditionen | None = None
    """
    Änderungen in den Vertragskonditionen. Falls in dieser Komponenten angegeben,
    werden die Tarifparameter hiermit überschrieben.
    """
    voraussetzungen: list[str] | None = Field(default=None, title="Voraussetzungen")
    """
    Voraussetzungen, die erfüllt sein müssen, damit dieser AufAbschlag zur Anwendung kommen kann
    """
    website: str | None = Field(default=None, title="Website")
    """
    Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    zusatzprodukte: list[str] | None = Field(default=None, title="Zusatzprodukte")
    """
    Zusatzprodukte, die nur in Kombination mit diesem AufAbschlag erhältlich sind
    """
