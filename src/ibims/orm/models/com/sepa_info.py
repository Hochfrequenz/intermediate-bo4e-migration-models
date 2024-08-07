import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

if TYPE_CHECKING:
    from ibims.orm.models.com.bankverbindung import Bankverbindung


class SepaInfo(SQLModel, table=True):
    """
    This class includes details about the sepa mandates.
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    sepa_id: str = Field(..., alias="sepaId", title="Sepaid")
    sepa_zahler: bool = Field(..., alias="sepaZahler", title="Sepazahler")
    creditor_identifier: str | None = Field(default=None, alias="creditorIdentifier", title="Creditoridentifier")
    gueltig_seit: datetime | None = Field(default=None, alias="gueltigSeit", title="Gueltigseit")
    sepainfo_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    bankverbindung_sepaInfo: List["Bankverbindung"] = Relationship(
        back_populates="sepaInfo",
        sa_relationship_kwargs={
            "primaryjoin": "Bankverbindung.sepaInfo_id==SepaInfo.sepainfo_sqlid",
            "lazy": "joined",
        },
    )
