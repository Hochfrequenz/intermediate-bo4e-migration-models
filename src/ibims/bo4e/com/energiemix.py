from pydantic import BaseModel, ConfigDict, Field

from ..enum.oekolabel import Oekolabel
from ..enum.oekozertifikat import Oekozertifikat
from ..enum.sparte import Sparte
from ..zusatz_attribut import ZusatzAttribut
from .energieherkunft import Energieherkunft


class Energiemix(BaseModel):
    """
    Zusammensetzung der gelieferten Energie aus den verschiedenen Primärenergieformen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Energiemix.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energiemix JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Energiemix.json>`_
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
    anteil: list[Energieherkunft] | None = Field(default=None, title="Anteil")
    """
    Anteile der jeweiligen Erzeugungsart
    """
    atommuell: float | None = Field(default=None, title="Atommuell")
    """
    Höhe des erzeugten Atommülls in g/kWh
    """
    bemerkung: str | None = Field(default=None, title="Bemerkung")
    """
    Bemerkung zum Energiemix
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Bezeichnung des Energiemix
    """
    co2_emission: float | None = Field(default=None, alias="co2Emission", title="Co2Emission")
    """
    Höhe des erzeugten CO2-Ausstosses in g/kWh
    """
    energieart: Sparte | None = None
    """
    Strom oder Gas etc.
    """
    energiemixnummer: int | None = Field(default=None, title="Energiemixnummer")
    """
    Eindeutige Nummer zur Identifizierung des Energiemixes
    """
    gueltigkeitsjahr: int | None = Field(default=None, title="Gueltigkeitsjahr")
    """
    Jahr, für das der Energiemix gilt
    """
    ist_in_oeko_top_ten: bool | None = Field(default=None, alias="istInOekoTopTen", title="Istinoekotopten")
    """
    Kennzeichen, ob der Versorger zu den Öko Top Ten gehört
    """
    oekolabel: list[Oekolabel] | None = Field(default=None, title="Oekolabel")
    """
    Ökolabel für den Energiemix
    """
    oekozertifikate: list[Oekozertifikat] | None = Field(default=None, title="Oekozertifikate")
    """
    Zertifikate für den Energiemix
    """
    website: str | None = Field(default=None, title="Website")
    """
    Internetseite, auf der die Strommixdaten veröffentlicht sind
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
