from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from ..enum.marktrolle import Marktrolle
from ..enum.verwendungszweck import Verwendungszweck


class VerwendungszweckProMarktrolle(BaseModel):
    """
    Dient zur Identifizierung des Verwendungszwecks der Marktrolle an der Marktlokation, der die Werte zu übermitteln sind.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Verwendungszweck.svg" type="image/svg+xml"></object>

    .. HINT::
        `Verwendungszweck JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Verwendungszweck.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
    )
    id: Annotated[str | None, Field(alias="_id", title=" Id")] = None
    version: Annotated[str | None, Field(alias="_version", title=" Version")] = "0.6.1rc14"
    marktrolle: Marktrolle | None = None
    zwecke: Annotated[list[Verwendungszweck] | None, Field(title="Zwecke")] = None
