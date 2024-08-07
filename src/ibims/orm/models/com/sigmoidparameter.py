import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import SigmoidparameterzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.preisstaffel import Preisstaffel
    from ibims.orm.models.com.regionale_preisstaffel import RegionalePreisstaffel
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Sigmoidparameter(SQLModel, table=True):
    """
    Die Sigmoid-Funktion, beispielsweise zur Berechnung eines Leistungspreises hat die Form:
    LP=A/(1+(P/B)^C)+D

    .. raw:: html

        <object data="../_static/images/bo4e/com/Sigmoidparameter.svg" type="image/svg+xml"></object>

    .. HINT::
        `Sigmoidparameter JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Sigmoidparameter.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    a: float | None = Field(default=None, alias="A", title="A")
    """
    Briefmarke Ortsverteilnetz (EUR/kWh)
    """
    b: float | None = Field(default=None, alias="B", title="B")
    """
    Briefmarke Ortsverteilnetz (EUR/kWh)
    """
    c: float | None = Field(default=None, alias="C", title="C")
    """
    Wendepunkt für die bepreiste Menge (kW)
    """
    d: float | None = Field(default=None, alias="D", title="D")
    """
    Exponent (einheitenlos)
    """
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
    sigmoidparameter_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    preisstaffel_sigmoidparameter: List["Preisstaffel"] = Relationship(
        back_populates="sigmoidparameter",
        sa_relationship_kwargs={
            "primaryjoin": "Preisstaffel.sigmoidparameter_id==Sigmoidparameter.sigmoidparameter_sqlid",
            "lazy": "joined",
        },
    )
    regionalepreisstaffel_sigmoidparameter: List["RegionalePreisstaffel"] = Relationship(
        back_populates="sigmoidparameter",
        sa_relationship_kwargs={
            "primaryjoin": "RegionalePreisstaffel.sigmoidparameter_id==Sigmoidparameter.sigmoidparameter_sqlid",
            "lazy": "joined",
        },
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="sigmoidparameter_zusatzattribute_link",
        link_model=SigmoidparameterzusatzAttributeLink,
    )
