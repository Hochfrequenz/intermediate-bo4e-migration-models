from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enum.mengeneinheit import Mengeneinheit
from ..enum.preisstatus import Preisstatus
from ..enum.waehrungseinheit import Waehrungseinheit

if TYPE_CHECKING:
    from ..zusatz_attribut import ZusatzAttribut


class Preis(BaseModel):
    """
    Abbildung eines Preises mit Wert, Einheit, Bezugswert und Status.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preis.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/com/Preis.json>`_
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
    bezugswert: Optional[Mengeneinheit] = None
    """
    Angabe, fÃ¼r welche BezugsgrÃ¶ÃŸe der Preis gilt. Z.B. kWh.
    """
    einheit: Optional[Waehrungseinheit] = None
    """
    WÃ¤hrungseinheit fÃ¼r den Preis, z.B. Euro oder Ct.
    """
    status: Optional[Preisstatus] = None
    """
    Gibt den Status des verÃ¶ffentlichten Preises an
    """
    wert: Optional[Decimal] = Field(default=None, title="Wert")
    """
    Gibt die nominale HÃ¶he des Preises an.
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
