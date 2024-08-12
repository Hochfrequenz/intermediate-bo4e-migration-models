from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..zusatz_attribut import ZusatzAttribut
    from .auf_abschlagstaffel_pro_ort import AufAbschlagstaffelProOrt


class AufAbschlagProOrt(BaseModel):
    """
    Mit dieser Komponente kÃ¶nnen Auf- und AbschlÃ¤ge verschiedener Typen im Zusammenhang
    mit Ã¶rtlichen GÃ¼ltigkeiten abgebildet werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/com/AufAbschlagProOrt.json>`_
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
    netznr: Optional[str] = Field(default=None, title="Netznr")
    """
    Die ene't-Netznummer des Netzes in dem der Aufschlag gilt.
    """
    ort: Optional[str] = Field(default=None, title="Ort")
    """
    Der Ort fÃ¼r den der Aufschlag gilt.
    """
    postleitzahl: Optional[str] = Field(default=None, title="Postleitzahl")
    """
    Die Postleitzahl des Ortes fÃ¼r den der Aufschlag gilt.
    """
    staffeln: Optional[list["AufAbschlagstaffelProOrt"]] = Field(default=None, title="Staffeln")
    """
    Werte fÃ¼r die gestaffelten Auf/AbschlÃ¤ge mit regionaler Eingrenzung.
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
