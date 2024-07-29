import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import MarktgebietInfozusatzAttributeLink, StandorteigenschaftenGasmarktgebieteLink

if TYPE_CHECKING:
    from ibims.orm.models.com.standorteigenschaften_gas import StandorteigenschaftenGas
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class MarktgebietInfo(SQLModel, table=True):
    """
    Informationen zum Marktgebiet im Gas.

    .. raw:: html

        <object data="../_static/images/bo4e/com/MarktgebietInfo.svg" type="image/svg+xml"></object>

    .. HINT::
        `MarktgebietInfo JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/MarktgebietInfo.json>`_
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
    marktgebiet: str | None = Field(default=None, title="Marktgebiet")
    """
    Der Name des Marktgebietes
    """
    marktgebietcode: str | None = Field(default=None, title="Marktgebietcode")
    """
    Der Name des Marktgebietes
    """
    marktgebietinfo_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="marktgebietinfo_zusatzattribute_link",
        link_model=MarktgebietInfozusatzAttributeLink,
    )
    standorteigenschaftengas_marktgebiete_link: List["StandorteigenschaftenGas"] = Relationship(
        back_populates="marktgebiete",
        link_model=StandorteigenschaftenGasmarktgebieteLink,
    )
