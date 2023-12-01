from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from ..enum.abgabe_art import AbgabeArt


class Konzessionsabgabe(BaseModel):
    """
    Diese Komponente wird zur Übertagung der Details zu einer Konzessionsabgabe verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Konzessionsabgabe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Konzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Konzessionsabgabe.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
    )
    id: Annotated[str | None, Field(alias="_id", title=" Id")] = None
    version: Annotated[str | None, Field(alias="_version", title=" Version")] = "0.6.1rc14"
    kategorie: Annotated[str | None, Field(title="Kategorie")] = None
    kosten: Annotated[float | str | None, Field(title="Kosten")] = None
    satz: AbgabeArt | None = None
