from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..zusatz_attribut import ZusatzAttribut
    from .betrag import Betrag
    from .menge import Menge
    from .preis import Preis


class Angebotsposition(BaseModel):
    """
    Unterhalb von Angebotsteilen sind die Angebotspositionen eingebunden.
    Hier werden die angebotenen Bestandteile einzeln aufgefÃ¼hrt. Beispiel:
    Positionsmenge: 4000 kWh
    Positionspreis: 24,56 ct/kWh
    Positionskosten: 982,40 EUR

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/com/Angebotsposition.json>`_
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
    positionsbezeichnung: Optional[str] = Field(default=None, title="Positionsbezeichnung")
    """
    Bezeichnung der jeweiligen Position des Angebotsteils
    """
    positionskosten: Optional["Betrag"] = None
    """
    Kosten (positionspreis * positionsmenge) fÃ¼r diese Angebotsposition
    """
    positionsmenge: Optional["Menge"] = None
    """
    Menge des angebotenen Artikels (z.B. Wirkarbeit in kWh), in dieser Angebotsposition
    """
    positionspreis: Optional["Preis"] = None
    """
    Preis pro Einheit/StÃ¼ckpreis des angebotenen Artikels.
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
