from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from ..com.externe_referenz import ExterneReferenz
from ..enum.geraeteklasse import Geraeteklasse
from ..enum.geraetetyp import Geraetetyp
from ..enum.typ import Typ


class Geraet(BaseModel):
    """
    Mit diesem BO werden alle Geräte modelliert, die keine Zähler sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geraet.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geraet JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Geraet.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
    )
    id: Annotated[str | None, Field(alias="_id", title=" Id")] = None
    typ: Annotated[Typ | None, Field(alias="_typ")] = Typ.GERAET
    version: Annotated[str | None, Field(alias="_version", title=" Version")] = "0.6.1rc14"
    bezeichnung: Annotated[str | None, Field(title="Bezeichnung")] = None
    externe_referenzen: Annotated[
        list[ExterneReferenz] | None, Field(alias="externeReferenzen", title="Externereferenzen")
    ] = None
    geraeteklasse: Geraeteklasse | None = None
    geraetenummer: Annotated[str | None, Field(title="Geraetenummer")] = None
    geraetetyp: Geraetetyp | None = None
