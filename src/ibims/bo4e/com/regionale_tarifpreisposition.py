from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enum.mengeneinheit import Mengeneinheit
from ..enum.preistyp import Preistyp
from ..enum.waehrungseinheit import Waehrungseinheit

if TYPE_CHECKING:
    from ..zusatz_attribut import ZusatzAttribut
    from .regionale_preisstaffel import RegionalePreisstaffel


class RegionaleTarifpreisposition(BaseModel):
    """
    Mit dieser Komponente kÃ¶nnen Tarifpreise verschiedener Typen im Zusammenhang mit regionalen GÃ¼ltigkeiten abgebildet
    werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionaleTarifpreisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionaleTarifpreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/com/RegionaleTarifpreisposition.json>`_
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
    bezugseinheit: Optional[Mengeneinheit] = None
    """
    GrÃ¶ÃŸe, auf die sich die Einheit bezieht, beispielsweise kWh, Jahr
    """
    einheit: Optional[Waehrungseinheit] = None
    """
    Einheit des Preises (z.B. EURO)
    """
    mengeneinheitstaffel: Optional[Mengeneinheit] = None
    """
    Gibt an, nach welcher Menge die vorgenannte EinschrÃ¤nkung erfolgt (z.B. Jahresstromverbrauch in kWh)
    """
    preisstaffeln: Optional[list["RegionalePreisstaffel"]] = Field(default=None, title="Preisstaffeln")
    """
    Hier sind die Staffeln mit ihren Preisangaben und regionalen GÃ¼ltigkeiten definiert
    """
    preistyp: Optional[Preistyp] = None
    """
    Angabe des Preistypes (z.B. Grundpreis)
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
