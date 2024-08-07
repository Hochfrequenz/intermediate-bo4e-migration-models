import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.arithmetische_operation import ArithmetischeOperation
from ibims.orm.models.many import MesslokationszuordnungzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.marktlokation import Marktlokation
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Messlokationszuordnung(SQLModel, table=True):
    """
    Mit dieser Komponente werden Messlokationen zu Marktlokationen zugeordnet.
    Dabei kann eine arithmetische Operation (Addition, Subtraktion, Multiplikation, Division) angegeben werden,
    mit der die Messlokation zum Verbrauch der Marktlokation beiträgt.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Messlokationszuordnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokationszuordnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Messlokationszuordnung.json>`_
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
    gueltig_bis: datetime | None = Field(default=None, alias="gueltigBis", title="Gueltigbis")
    """
    exklusives Endedatum
    """
    gueltig_seit: datetime | None = Field(default=None, alias="gueltigSeit", title="Gueltigseit")
    """
    gueltig_bis: Optional[pydantic.AwareDatetime] = None
    """
    messlokations_id: str | None = Field(default=None, alias="messlokationsId", title="Messlokationsid")
    """
    arithmetik: Optional["ArithmetischeOperation"] = None

    gueltig_seit: Optional[pydantic.AwareDatetime] = None
    """
    messlokationszuordnung_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    marktlokation_zugehoerigeMesslokation: List["Marktlokation"] = Relationship(
        back_populates="zugehoerigeMesslokation",
        sa_relationship_kwargs={
            "primaryjoin": "Marktlokation.zugehoerigeMesslokation_id==Messlokationszuordnung.messlokationszuordnung_sqlid",
            "lazy": "joined",
        },
    )
    arithmetik: ArithmetischeOperation | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="messlokationszuordnung_zusatzattribute_link",
        link_model=MesslokationszuordnungzusatzAttributeLink,
    )
