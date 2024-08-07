import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

if TYPE_CHECKING:
    from ibims.orm.models.com.sepa_info import SepaInfo


class Bankverbindung(SQLModel, table=True):
    """
    This component contains bank connection information.
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    iban: str | None = Field(default=None, title="Iban")
    bic: str | None = Field(default=None, title="Bic")
    gueltig_seit: datetime | None = Field(default=None, alias="gueltigSeit", title="Gueltigseit")
    gueltig_bis: datetime | None = Field(default=None, alias="gueltigBis", title="Gueltigbis")
    bankname: str | None = Field(default=None, title="Bankname")
    kontoinhaber: str | None = Field(default=None, title="Kontoinhaber")
    ouid: int = Field(..., title="Ouid")
    bankverbindung_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    sepaInfo_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("sepainfo.sepainfo_sqlid", ondelete="SET NULL"),
        )
    )
    sepaInfo: "SepaInfo" = Relationship(
        back_populates="bankverbindung_sepaInfo",
        sa_relationship_kwargs={"foreign_keys": "[Bankverbindung.sepaInfo_id]"},
    )
