import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.gueltigkeitstyp import Gueltigkeitstyp
from ibims.orm.models.many import RegionaleGueltigkeitkriteriumsWerteLink, RegionaleGueltigkeitzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.kriterium_wert import KriteriumWert
    from ibims.orm.models.com.regionale_preisgarantie import RegionalePreisgarantie
    from ibims.orm.models.com.regionale_preisstaffel import RegionalePreisstaffel
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class RegionaleGueltigkeit(SQLModel, table=True):
    """
    Mit dieser Komponente können regionale Gültigkeiten, z.B. für Tarife, Zu- und Abschläge und Preise definiert werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionaleGueltigkeit.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionaleGueltigkeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/RegionaleGueltigkeit.json>`_
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
    regionalegueltigkeit_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    gueltigkeitstyp: Gueltigkeitstyp | None = Field(None)
    kriteriumsWerte: List["KriteriumWert"] = Relationship(
        back_populates="regionalegueltigkeit_kriteriumswerte_link",
        link_model=RegionaleGueltigkeitkriteriumsWerteLink,
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="regionalegueltigkeit_zusatzattribute_link",
        link_model=RegionaleGueltigkeitzusatzAttributeLink,
    )
    regionalepreisgarantie_regionaleGueltigkeit: List["RegionalePreisgarantie"] = Relationship(
        back_populates="regionaleGueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "RegionalePreisgarantie.regionaleGueltigkeit_id==RegionaleGueltigkeit.regionalegueltigkeit_sqlid",
            "lazy": "joined",
        },
    )
    regionalepreisstaffel_regionaleGueltigkeit: List["RegionalePreisstaffel"] = Relationship(
        back_populates="regionaleGueltigkeit",
        sa_relationship_kwargs={
            "primaryjoin": "RegionalePreisstaffel.regionaleGueltigkeit_id==RegionaleGueltigkeit.regionalegueltigkeit_sqlid",
            "lazy": "joined",
        },
    )
