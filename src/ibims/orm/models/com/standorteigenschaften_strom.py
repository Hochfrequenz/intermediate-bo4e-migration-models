import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import (
    StandorteigenschafteneigenschaftenStromLink,
    StandorteigenschaftenStromzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.standorteigenschaften import Standorteigenschaften
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class StandorteigenschaftenStrom(SQLModel, table=True):
    """
    Standorteigenschaften der Sparte Strom

    .. raw:: html

        <object data="../_static/images/bo4e/com/StandorteigenschaftenStrom.svg" type="image/svg+xml"></object>

    .. HINT::
        `StandorteigenschaftenStrom JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/StandorteigenschaftenStrom.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
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
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    bilanzierungsgebiet_eic: str | None = Field(
        default=None, alias="bilanzierungsgebietEic", title="Bilanzierungsgebieteic"
    )
    """
    Die EIC-Nummer des Bilanzierungsgebietes
    """
    regelzone: str | None = Field(default=None, title="Regelzone")
    """
    Der Name der Regelzone
    """
    regelzone_eic: str | None = Field(default=None, alias="regelzoneEic", title="Regelzoneeic")
    """
    De EIC-Nummer der Regelzone
    """
    standorteigenschaftenstrom_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    standorteigenschaften_eigenschaftenstrom_link: List["Standorteigenschaften"] = Relationship(
        back_populates="eigenschaftenStrom",
        link_model=StandorteigenschafteneigenschaftenStromLink,
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="standorteigenschaftenstrom_zusatzattribute_link",
        link_model=StandorteigenschaftenStromzusatzAttributeLink,
    )
