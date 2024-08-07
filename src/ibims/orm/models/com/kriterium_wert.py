import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.tarifregionskriterium import Tarifregionskriterium
from ibims.orm.models.many import KriteriumWertzusatzAttributeLink, RegionaleGueltigkeitkriteriumsWerteLink

if TYPE_CHECKING:
    from ibims.orm.models.com.regionale_gueltigkeit import RegionaleGueltigkeit
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class KriteriumWert(SQLModel, table=True):
    """
    Mit dieser Komponente können Kriterien und deren Werte definiert werden

    .. raw:: html

        <object data="../_static/images/bo4e/com/KriteriumWert.svg" type="image/svg+xml"></object>

    .. HINT::
        `KriteriumWert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/KriteriumWert.json>`_
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
    wert: str | None = Field(default=None, title="Wert")
    """
    Ein Wert, passend zum Kriterium. Z.B. eine Postleitzahl.
    """
    kriteriumwert_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    kriterium: Tarifregionskriterium | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="kriteriumwert_zusatzattribute_link",
        link_model=KriteriumWertzusatzAttributeLink,
    )
    regionalegueltigkeit_kriteriumswerte_link: List["RegionaleGueltigkeit"] = Relationship(
        back_populates="kriteriumsWerte",
        link_model=RegionaleGueltigkeitkriteriumsWerteLink,
    )
