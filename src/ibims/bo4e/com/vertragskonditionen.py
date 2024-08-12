from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..zusatz_attribut import ZusatzAttribut
    from .zeitraum import Zeitraum


class Vertragskonditionen(BaseModel):
    """
    Abbildung fÃ¼r Vertragskonditionen. Die Komponente wird sowohl im Vertrag als auch im Tarif verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Vertragskonditionen.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertragskonditionen JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/com/Vertragskonditionen.json>`_
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
    abschlagszyklus: Optional["Zeitraum"] = None
    """
    In diesen Zyklen werden AbschlÃ¤ge gestellt. Alternativ kann auch die Anzahl in den Konditionen angeben werden.
    """
    anzahl_abschlaege: Optional[Decimal] = Field(default=None, alias="anzahlAbschlaege", title="Anzahlabschlaege")
    """
    Anzahl der vereinbarten AbschlÃ¤ge pro Jahr, z.B. 12
    """
    beschreibung: Optional[str] = Field(default=None, title="Beschreibung")
    """
    Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen Gas"
    """
    kuendigungsfrist: Optional["Zeitraum"] = None
    """
    Innerhalb dieser Frist kann der Vertrag gekÃ¼ndigt werden
    """
    vertragslaufzeit: Optional["Zeitraum"] = None
    """
    Ãœber diesen Zeitraum lÃ¤uft der Vertrag
    """
    vertragsverlaengerung: Optional["Zeitraum"] = None
    """
    Falls der Vertrag nicht gekÃ¼ndigt wird, verlÃ¤ngert er sich automatisch um die hier angegebene Zeit
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
