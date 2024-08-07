import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.enum.preistyp import Preistyp
from ibims.orm.models.enum.waehrungseinheit import Waehrungseinheit
from ibims.orm.models.many import (
    RegionaleTarifpreispositionpreisstaffelnLink,
    RegionaleTarifpreispositionzusatzAttributeLink,
    RegionaltariftarifpreiseLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.regionaltarif import Regionaltarif
    from ibims.orm.models.com.regionale_preisstaffel import RegionalePreisstaffel
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class RegionaleTarifpreisposition(SQLModel, table=True):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen im Zusammenhang mit regionalen Gültigkeiten abgebildet
    werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionaleTarifpreisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionaleTarifpreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/RegionaleTarifpreisposition.json>`_
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
    regionaletarifpreisposition_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    regionaltarif_tarifpreise_link: List["Regionaltarif"] = Relationship(
        back_populates="tarifpreise", link_model=RegionaltariftarifpreiseLink
    )
    bezugseinheit: Mengeneinheit | None = Field(None)
    einheit: Waehrungseinheit | None = Field(None)
    mengeneinheitstaffel: Mengeneinheit | None = Field(None)
    preisstaffeln: List["RegionalePreisstaffel"] = Relationship(
        back_populates="regionaletarifpreisposition_preisstaffeln_link",
        link_model=RegionaleTarifpreispositionpreisstaffelnLink,
    )
    preistyp: Preistyp | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="regionaletarifpreisposition_zusatzattribute_link",
        link_model=RegionaleTarifpreispositionzusatzAttributeLink,
    )
