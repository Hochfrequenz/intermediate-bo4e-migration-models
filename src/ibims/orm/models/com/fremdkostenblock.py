import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import (
    FremdkostenblockkostenpositionenLink,
    FremdkostenblockzusatzAttributeLink,
    FremdkostenkostenbloeckeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.bo.fremdkosten import Fremdkosten
    from ibims.orm.models.com.betrag import Betrag
    from ibims.orm.models.com.fremdkostenposition import Fremdkostenposition
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Fremdkostenblock(SQLModel, table=True):
    """
    Komponente zur Abbildung eines Kostenblocks in den Fremdkosten

    .. raw:: html

        <object data="../_static/images/bo4e/com/Fremdkostenblock.svg" type="image/svg+xml"></object>

    .. HINT::
        `Fremdkostenblock JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Fremdkostenblock.json>`_
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
    kostenblockbezeichnung: str | None = Field(default=None, title="Kostenblockbezeichnung")
    """
    Bezeichnung für einen Kostenblock. Z.B. Netzkosten, Messkosten, Umlagen, etc.
    """
    fremdkostenblock_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    fremdkosten_kostenbloecke_link: List["Fremdkosten"] = Relationship(
        back_populates="kostenbloecke", link_model=FremdkostenkostenbloeckeLink
    )
    kostenpositionen: List["Fremdkostenposition"] = Relationship(
        back_populates="fremdkostenblock_kostenpositionen_link",
        link_model=FremdkostenblockkostenpositionenLink,
    )
    summeKostenblock_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("betrag.betrag_sqlid", ondelete="SET NULL"))
    )
    summeKostenblock: "Betrag" = Relationship(
        back_populates="fremdkostenblock_summeKostenblock",
        sa_relationship_kwargs={"foreign_keys": "[Fremdkostenblock.summeKostenblock_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="fremdkostenblock_zusatzattribute_link",
        link_model=FremdkostenblockzusatzAttributeLink,
    )
