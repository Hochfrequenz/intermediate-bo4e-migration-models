from pydantic import BaseModel, ConfigDict, Field

from ..com.adresse import Adresse
from ..com.dienstleistung import Dienstleistung
from ..com.geokoordinaten import Geokoordinaten
from ..com.katasteradresse import Katasteradresse
from ..enum.netzebene import Netzebene
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut
from .geraet import Geraet
from .zaehler import Zaehler


class Messlokation(BaseModel):
    """
    Object containing information about a Messlokation

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Messlokation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Messlokation.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.MESSLOKATION, alias="_typ")
    """
    Die Messlokations-Identifikation; Das ist die frühere Zählpunktbezeichnung
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    geoadresse: Geokoordinaten | None = None
    """
    katasterinformation: Optional["Katasteradresse"] = None
    """
    geraete: list[Geraet] | None = Field(default=None, title="Geraete")
    """
    Liste der Geräte, die zu dieser Messstelle gehört
    """
    grundzustaendiger_msb_codenr: str | None = Field(
        default=None,
        alias="grundzustaendigerMsbCodenr",
        title="Grundzustaendigermsbcodenr",
    )
    """
    grundzustaendiger_msbim_codenr: Optional[str] = None
    """
    grundzustaendiger_msbim_codenr: str | None = Field(
        default=None,
        alias="grundzustaendigerMsbimCodenr",
        title="Grundzustaendigermsbimcodenr",
    )
    """
    # only one of the following three optional address attributes can be set
    messadresse: Optional["Adresse"] = None
    """
    katasterinformation: Katasteradresse | None = None
    """
    Alternativ zu einer postalischen Adresse und Geokoordinaten kann hier eine Ortsangabe mittels Gemarkung und
    Flurstück erfolgen.
    """
    messadresse: Adresse | None = None
    """
    geoadresse: Optional["Geokoordinaten"] = None
    """
    messdienstleistung: list[Dienstleistung] | None = Field(default=None, title="Messdienstleistung")
    """
    Liste der Messdienstleistungen, die zu dieser Messstelle gehört
    """
    messgebietnr: str | None = Field(default=None, title="Messgebietnr")
    """
    Die Nummer des Messgebietes in der ene't-Datenbank
    """
    messlokations_id: str = Field(..., alias="messlokationsId", title="Messlokationsid")
    """
    Die Messlokations-Identifikation; Das ist die frühere Zählpunktbezeichnung
    """
    messlokationszaehler: list[Zaehler] | None = Field(default=None, title="Messlokationszaehler")
    """
    Zähler, die zu dieser Messlokation gehören
    """
    netzebene_messung: Netzebene | None = Field(default=None, alias="netzebeneMessung")
    """
    Spannungsebene der Messung
    """
    sparte: Sparte | None = None
    """
    Sparte der Messlokation, z.B. Gas oder Strom
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
