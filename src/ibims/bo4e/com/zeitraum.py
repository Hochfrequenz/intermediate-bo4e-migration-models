from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..enum.mengeneinheit import Mengeneinheit
from ..zusatz_attribut import ZusatzAttribut


class Zeitraum(BaseModel):
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher eine der drei Möglichkeiten angegeben sein:
    - Einheit und Dauer oder
    - Zeitraum: Startdatum bis Enddatum oder
    - Zeitraum: Startzeitpunkt (Datum und Uhrzeit) bis Endzeitpunkt (Datum und Uhrzeit)

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitraum.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitraum JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Zeitraum.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(
        default=None,
        alias="_id",
        description='zusatz_attribute: Optional[list["ZusatzAttribut"]] = None\n\n# pylint: disable=duplicate-code\nmodel_config = ConfigDict(\n    alias_generator=camelize,\n    populate_by_name=True,\n    extra="allow",\n    # json_encoders is deprecated, but there is no easy-to-use alternative. The best way would be to create\n    # an annotated version of Decimal, but you would have to use it everywhere in the pydantic models.\n    # See this issue for more info: https://github.com/pydantic/pydantic/issues/6375\n    json_encoders={Decimal: str},\n)',
        title=" Id",
    )
    version: str | None = Field(
        default="v202401.2.1",
        alias="_version",
        description='Version der BO-Struktur aka "fachliche Versionierung"',
        title=" Version",
    )
    dauer: float | None = Field(default=None, title="Dauer")
    einheit: Mengeneinheit | None = None
    enddatum: datetime | None = Field(default=None, title="Enddatum")
    endzeitpunkt: datetime | None = Field(default=None, title="Endzeitpunkt")
    startdatum: datetime | None = Field(default=None, title="Startdatum")
    startzeitpunkt: datetime | None = Field(default=None, title="Startzeitpunkt")
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
