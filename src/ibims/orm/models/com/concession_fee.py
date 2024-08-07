import uuid as uuid_pkg
from datetime import datetime

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig


class ConcessionFee(SQLModel, table=True):
    """
    The Concession Fee object was created during a migration project.
    It contains attributes needed for metering mapping.
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    market_location_id: str = Field(..., alias="marketLocationId", title="Marketlocationid")
    group: str | None = Field(default=None, title="Group")
    obis: str = Field(..., title="Obis")
    active_from: datetime = Field(..., alias="activeFrom", title="Activefrom")
    active_until: datetime | None = Field(default=None, alias="activeUntil", title="Activeuntil")
    ka: str | None = Field(default=None, title="Ka")
    concessionfee_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
