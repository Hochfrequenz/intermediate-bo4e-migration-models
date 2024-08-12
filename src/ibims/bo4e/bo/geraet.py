from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enum.geraeteklasse import Geraeteklasse
from ..enum.geraetetyp import Geraetetyp
from ..enum.typ import Typ

if TYPE_CHECKING:
    from ..zusatz_attribut import ZusatzAttribut


class Geraet(BaseModel):
    """
    Mit diesem BO werden alle GerÃ¤te modelliert, die keine ZÃ¤hler sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geraet.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geraet JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/bo/Geraet.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: Optional[str] = Field(default=None, alias="_id", title=" Id")
    """
    Hier kÃ¶nnen IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    typ: Typ = Field(default=Typ.GERAET, alias="_typ")
    """
    Die auf dem GerÃ¤t aufgedruckte Nummer, die vom MSB vergeben wird.
    """
    version: str = Field(default="v202401.4.0", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    bezeichnung: Optional[str] = Field(default=None, title="Bezeichnung")
    """
    Bezeichnung des GerÃ¤ts
    """
    geraeteklasse: Optional[Geraeteklasse] = None
    """
    Die Ã¼bergreifende Klasse eines GerÃ¤ts, beispielsweise Wandler
    """
    geraetenummer: Optional[str] = Field(default=None, title="Geraetenummer")
    """
    Die auf dem GerÃ¤t aufgedruckte Nummer, die vom MSB vergeben wird.
    """
    geraetetyp: Optional[Geraetetyp] = None
    """
    Der speziellere Typ eines GerÃ¤tes, beispielsweise Stromwandler
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
