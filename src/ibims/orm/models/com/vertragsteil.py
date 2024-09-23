import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import VertragsteilzusatzAttributeLink, VertragvertragsteileLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.vertrag import Vertrag
    from ibims.orm.models.com.menge import Menge
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Vertragsteil(SQLModel, table=True):
    """
    Abbildung für einen Vertragsteil. Der Vertragsteil wird dazu verwendet,
    eine vertragliche Leistung in Bezug zu einer Lokation (Markt- oder Messlokation) festzulegen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Vertragsteil.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertragsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Vertragsteil.json>`_
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
    lokation: str | None = Field(default=None, title="Lokation")
    """
    vertraglich_fixierte_menge: Optional["Menge"] = None
    """
    vertragsteilbeginn: datetime | None = Field(default=None, title="Vertragsteilbeginn")
    """
    vertragsteilende: Optional[pydantic.AwareDatetime] = None
    """
    vertragsteilende: datetime | None = Field(default=None, title="Vertragsteilende")
    """
    lokation: Optional[str] = None
    """
    vertragsteil_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    vertrag_vertragsteile_link: List["Vertrag"] = Relationship(
        back_populates="vertragsteile", link_model=VertragvertragsteileLink
    )
    maximaleAbnahmemenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    maximaleAbnahmemenge: "Menge" = Relationship(
        back_populates="vertragsteil_maximaleAbnahmemenge",
        sa_relationship_kwargs={"foreign_keys": "[Vertragsteil.maximaleAbnahmemenge_id]"},
    )
    minimaleAbnahmemenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    minimaleAbnahmemenge: "Menge" = Relationship(
        back_populates="vertragsteil_minimaleAbnahmemenge",
        sa_relationship_kwargs={"foreign_keys": "[Vertragsteil.minimaleAbnahmemenge_id]"},
    )
    vertraglichFixierteMenge_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("menge.menge_sqlid", ondelete="SET NULL"))
    )
    vertraglichFixierteMenge: "Menge" = Relationship(
        back_populates="vertragsteil_vertraglichFixierteMenge",
        sa_relationship_kwargs={"foreign_keys": "[Vertragsteil.vertraglichFixierteMenge_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="vertragsteil_zusatzattribute_link",
        link_model=VertragsteilzusatzAttributeLink,
    )
