from pydantic import BaseModel, ConfigDict, Field

from ..enum.preismodell import Preismodell
from ..enum.rechnungslegung import Rechnungslegung
from ..enum.sparte import Sparte
from ..enum.vertragsform import Vertragsform
from ..zusatz_attribut import ZusatzAttribut
from .ausschreibungsdetail import Ausschreibungsdetail
from .menge import Menge
from .zeitraum import Zeitraum


class Ausschreibungslos(BaseModel):
    """
    Eine Komponente zur Abbildung einzelner Lose einer Ausschreibung

    .. raw:: html

        <object data="../_static/images/bo4e/com/Ausschreibungslos.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibungslos JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Ausschreibungslos.json>`_
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
    anzahl_lieferstellen: int | None = Field(default=None, alias="anzahlLieferstellen", title="Anzahllieferstellen")
    """
    Anzahl der Lieferstellen in dieser Ausschreibung
    """
    bemerkung: str | None = Field(default=None, title="Bemerkung")
    """
    Bemerkung des Kunden zum Los
    """
    betreut_durch: str | None = Field(default=None, alias="betreutDurch", title="Betreutdurch")
    """
    Name des Lizenzpartners
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Bezeichnung der Ausschreibung
    """
    energieart: Sparte | None = None
    """
    Unterscheidungsmöglichkeiten für die Sparte
    """
    gesamt_menge: Menge | None = Field(default=None, alias="gesamtMenge")
    """
    Gibt den Gesamtjahresverbrauch (z.B. in kWh) aller in diesem Los enthaltenen Lieferstellen an
    """
    lieferstellen: list[Ausschreibungsdetail] | None = Field(default=None, title="Lieferstellen")
    """
    Die ausgeschriebenen Lieferstellen
    """
    lieferzeitraum: Zeitraum | None = None
    """
    Zeitraum, für den die in diesem Los enthaltenen Lieferstellen beliefert werden sollen
    """
    losnummer: str | None = Field(default=None, title="Losnummer")
    """
    Laufende Nummer des Loses
    """
    preismodell: Preismodell | None = None
    """
    Bezeichnung der Preismodelle in Ausschreibungen für die Energielieferung
    """
    wiederholungsintervall: Zeitraum | None = None
    """
    Kundenwunsch zur Kündigungsfrist in der Ausschreibung
    """
    wunsch_kuendingungsfrist: Zeitraum | None = Field(default=None, alias="wunschKuendingungsfrist")
    """
    Kundenwunsch zur Kündigungsfrist in der Ausschreibung
    """
    wunsch_maximalmenge: Menge | None = Field(default=None, alias="wunschMaximalmenge")
    """
    Maximalmenge Toleranzband (kWh, %)
    """
    wunsch_mindestmenge: Menge | None = Field(default=None, alias="wunschMindestmenge")
    """
    Mindesmenge Toleranzband (kWh, %)
    """
    wunsch_rechnungslegung: Rechnungslegung | None = Field(default=None, alias="wunschRechnungslegung")
    """
    Aufzählung der Möglichkeiten zur Rechnungslegung in Ausschreibungen
    """
    wunsch_vertragsform: Vertragsform | None = Field(default=None, alias="wunschVertragsform")
    """
    Aufzählung der Möglichkeiten zu Vertragsformen in Ausschreibungen
    """
    wunsch_zahlungsziel: Zeitraum | None = Field(default=None, alias="wunschZahlungsziel")
    """
    Kundenwunsch zum Zahlungsziel in der Ausschreibung
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
