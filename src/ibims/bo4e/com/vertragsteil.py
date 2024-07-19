from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..zusatz_attribut import ZusatzAttribut
from .menge import Menge


class Vertragsteil(BaseModel):
    """
    Abbildung für einen Vertragsteil. Der Vertragsteil wird dazu verwendet,
    eine vertragliche Leistung in Bezug zu einer Lokation (Markt- oder Messlokation) festzulegen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Vertragsteil.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertragsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Vertragsteil.json>`_
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = None

    # pylint: disable=duplicate-code
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        extra="allow",
        # json_encoders is deprecated, but there is no easy-to-use alternative. The best way would be to create
        # an annotated version of Decimal, but you would have to use it everywhere in the pydantic models.
        # See this issue for more info: https://github.com/pydantic/pydantic/issues/6375
        json_encoders={Decimal: str},
    )
    """
    version: str = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    lokation: str | None = Field(default=None, title="Lokation")
    """
    vertraglich_fixierte_menge: Optional["Menge"] = None
    """
    maximale_abnahmemenge: Menge | None = Field(default=None, alias="maximaleAbnahmemenge")
    """
    Für die Lokation festgelegte maximale Abnahmemenge (exklusiv)
    """
    minimale_abnahmemenge: Menge | None = Field(default=None, alias="minimaleAbnahmemenge")
    """
    maximale_abnahmemenge: Optional["Menge"] = None
    """
    vertraglich_fixierte_menge: Menge | None = Field(default=None, alias="vertraglichFixierteMenge")
    """
    minimale_abnahmemenge: Optional["Menge"] = None
    """
    vertragsteilbeginn: datetime | None = Field(default=None, title="Vertragsteilbeginn")
    """
    vertragsteilende: Optional[pydantic.AwareDatetime] = None
    """
    vertragsteilende: datetime | None = Field(default=None, title="Vertragsteilende")
    """
    lokation: Optional[str] = None
    """
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="Zusatzattribute"
    )
