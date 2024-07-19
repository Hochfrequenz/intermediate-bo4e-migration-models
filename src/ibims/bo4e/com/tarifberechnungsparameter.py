from pydantic import BaseModel, ConfigDict, Field

from ..enum.messpreistyp import Messpreistyp
from ..enum.tarifkalkulationsmethode import Tarifkalkulationsmethode
from ..zusatz_attribut import ZusatzAttribut
from .preis import Preis
from .tarifpreis import Tarifpreis


class Tarifberechnungsparameter(BaseModel):
    """
    In dieser Komponente sind die Berechnungsparameter für die Ermittlung der Tarifkosten zusammengefasst.
    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifberechnungsparameter.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifberechnungsparameter JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Tarifberechnungsparameter.json>`_
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
    berechnungsmethode: Tarifkalkulationsmethode | None = None
    """
    Gibt an, wie die Einzelpreise des Tarifes zu verarbeiten sind
    """
    hoechstpreis_ht: Preis | None = Field(default=None, alias="hoechstpreisHT")
    """
    Höchstpreis für den Durchschnitts-Arbeitspreis HT
    """
    hoechstpreis_nt: Preis | None = Field(default=None, alias="hoechstpreisNT")
    """
    Höchstpreis für den Durchschnitts-Arbeitspreis NT
    """
    ist_messpreis_in_grundpreis_enthalten: bool | None = Field(
        default=None,
        alias="istMesspreisInGrundpreisEnthalten",
        title="Istmesspreisingrundpreisenthalten",
    )
    """
    True, falls der Messpreis im Grundpreis (GP) enthalten ist
    """
    ist_messpreis_zu_beruecksichtigen: bool | None = Field(
        default=None,
        alias="istMesspreisZuBeruecksichtigen",
        title="Istmesspreiszuberuecksichtigen",
    )
    """
    Typ des Messpreises
    """
    kw_inklusive: float | None = Field(default=None, alias="kwInklusive", title="Kwinklusive")
    """
    Im Preis bereits eingeschlossene Leistung (für Gas)
    """
    kw_weitere_mengen: float | None = Field(default=None, alias="kwWeitereMengen", title="Kwweiteremengen")
    """
    Intervall, indem die über "kwInklusive" hinaus abgenommene Leistung kostenpflichtig wird (z.B. je 5 kW 20 EURO)
    """
    messpreistyp: Messpreistyp | None = None
    """
    Typ des Messpreises
    """
    mindestpreis: Preis | None = None
    """
    Mindestpreis für den Durchschnitts-Arbeitspreis
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
    zusatzpreise: list[Tarifpreis] | None = Field(default=None, title="Zusatzpreise")
    """
    Liste mit zusätzlichen Preisen, beispielsweise Messpreise und/oder Leistungspreise
    """
