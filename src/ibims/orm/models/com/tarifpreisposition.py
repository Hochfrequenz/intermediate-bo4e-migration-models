import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.enum.preistyp import Preistyp
from ibims.orm.models.enum.waehrungseinheit import Waehrungseinheit
from ibims.orm.models.many import (
    TarifpreisblatttarifpreiseLink,
    TarifpreispositionpreisstaffelnLink,
    TarifpreispositionzusatzAttributeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.tarifpreisblatt import Tarifpreisblatt
    from ibims.orm.models.com.preisstaffel import Preisstaffel
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Tarifpreisposition(SQLModel, table=True):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifpreisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifpreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Tarifpreisposition.json>`_
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
    tarifpreisposition_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    tarifpreisblatt_tarifpreise_link: List["Tarifpreisblatt"] = Relationship(
        back_populates="tarifpreise", link_model=TarifpreisblatttarifpreiseLink
    )
    bezugseinheit: Mengeneinheit | None = Field(None)
    einheit: Waehrungseinheit | None = Field(None)
    mengeneinheitstaffel: Mengeneinheit | None = Field(None)
    preisstaffeln: List["Preisstaffel"] = Relationship(
        back_populates="tarifpreisposition_preisstaffeln_link",
        link_model=TarifpreispositionpreisstaffelnLink,
    )
    preistyp: Preistyp | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="tarifpreisposition_zusatzattribute_link",
        link_model=TarifpreispositionzusatzAttributeLink,
    )
