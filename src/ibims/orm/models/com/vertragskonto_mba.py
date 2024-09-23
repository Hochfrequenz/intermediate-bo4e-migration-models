import uuid as uuid_pkg
from typing import TYPE_CHECKING, Any, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.kontaktart import Kontaktart

if TYPE_CHECKING:
    from ibims.orm.models.com.adresse import Adresse
    from ibims.orm.models.com.vertragskonto_cba import VertragskontoCBA


class VertragskontoMBA(SQLModel, table=True):
    """
    Models an MBA (master billing account). Its main purpose is to bundle CBAs together having the same address in
    their related contracts. This feature supports a single invoice for all CBAs instead of several
    invoices for each.
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    ouid: int = Field(..., title="Ouid")
    vertragskontonummer: str = Field(..., title="Vertragskontonummer")
    vertragskontomba_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    vertragsAdresse: "Adresse" = Relationship(
        back_populates="vertragskontomba_vertragsAdresse",
        sa_relationship_kwargs={"foreign_keys": "[VertragskontoMBA.vertragsAdresse_id]"},
    )
    vertragsAdresse_id: uuid_pkg.UUID = Field(
        sa_column=Column(UUID(as_uuid=True), ForeignKey("adresse.adresse_sqlid", ondelete="SET NULL"))
    )
    rechnungsstellung: Kontaktart = Field(None)
    cbas_id: uuid_pkg.UUID = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("vertragskontocba.vertragskontocba_sqlid", ondelete="SET NULL"),
        )
    )
    cbas: "VertragskontoCBA" = Relationship(
        back_populates="vertragskontomba_cbas",
        sa_relationship_kwargs={"foreign_keys": "[VertragskontoMBA.cbas_id]"},
    )
