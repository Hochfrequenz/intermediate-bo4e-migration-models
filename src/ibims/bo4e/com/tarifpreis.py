from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enum.mengeneinheit import Mengeneinheit
from ..enum.preisstatus import Preisstatus
from ..enum.preistyp import Preistyp
from ..enum.waehrungseinheit import Waehrungseinheit

if TYPE_CHECKING:
    from ..zusatz_attribut import ZusatzAttribut


class Tarifpreis(BaseModel):
    """
    Abbildung eines Tarifpreises mit Preistyp und Beschreibung abgeleitet von COM Preis.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifpreis.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifpreis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/com/Tarifpreis.json>`_
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
    beschreibung: Optional[str] = Field(default=None, title="Beschreibung")
    """
    Beschreibung des Preises. Hier kÃ¶nnen z.B. Preisdetails angegeben sein, beispielsweise "DrehstromzÃ¤hler".
    """
    bezugswert: Optional[Mengeneinheit] = None
    """
    Angabe, fÃ¼r welche BezugsgrÃ¶ÃŸe der Preis gilt. Z.B. kWh.
    """
    einheit: Optional[Waehrungseinheit] = None
    """
    WÃ¤hrungseinheit fÃ¼r den Preis, z.B. Euro oder Ct.
    """
    preistyp: Optional[Preistyp] = None
    """
    Angabe des Preistypes (z.B. Grundpreis)
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
