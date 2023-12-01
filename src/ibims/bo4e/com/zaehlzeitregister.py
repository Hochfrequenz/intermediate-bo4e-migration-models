from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated


class Zaehlzeitregister(BaseModel):
    """
    Mit dieser Komponente werden Zählzeitregister modelliert. Ein Zählzeitregister beschreibt eine erweiterte Definition der Zählzeit
    in Bezug auf ein Register. Dabei werden alle Codes dazu vom Netzbetreiber vergeben.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlzeitregister.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlzeitregister JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Zaehlzeitregister.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
    )
    id: Annotated[str | None, Field(alias="_id", title=" Id")] = None
    version: Annotated[str | None, Field(alias="_version", title=" Version")] = "0.6.1rc14"
    ist_schwachlastfaehig: Annotated[
        bool | None, Field(alias="istSchwachlastfaehig", title="Istschwachlastfaehig")
    ] = None
    zaehlzeit_definition: Annotated[str | None, Field(alias="zaehlzeitDefinition", title="Zaehlzeitdefinition")] = None
    zaehlzeit_register: Annotated[str | None, Field(alias="zaehlzeitRegister", title="Zaehlzeitregister")] = None
