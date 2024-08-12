from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..zusatz_attribut import ZusatzAttribut


class Zaehlzeitregister(BaseModel):
    """
    Mit dieser Komponente werden ZÃ¤hlzeitregister modelliert. Ein ZÃ¤hlzeitregister beschreibt eine erweiterte Definition der ZÃ¤hlzeit
    in Bezug auf ein Register. Dabei werden alle Codes dazu vom Netzbetreiber vergeben.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlzeitregister.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlzeitregister JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.4.0/src/bo4e_schemas/com/Zaehlzeitregister.json>`_
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
    ist_schwachlastfaehig: Optional[bool] = Field(
        default=None, alias="istSchwachlastfaehig", title="Istschwachlastfaehig"
    )
    """
    ZÃ¤hlzeitregister
    """
    zaehlzeit_definition: Optional[str] = Field(default=None, alias="zaehlzeitDefinition", title="Zaehlzeitdefinition")
    """
    ZÃ¤hlzeitdefinition
    """
    zaehlzeit_register: Optional[str] = Field(default=None, alias="zaehlzeitRegister", title="Zaehlzeitregister")
    """
    ZÃ¤hlzeitdefinition
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
