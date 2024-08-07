import uuid as uuid_pkg
from decimal import Decimal
from typing import Any

from pydantic import ConfigDict
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.mengeneinheit import Mengeneinheit


class Zaehlpunkt(SQLModel, table=True):
    """
    The zaehlpunkt object was created during a migration project.
    It contains attributes needed for metering mapping.
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    periodenverbrauch_vorhersage: Decimal = Field(
        ..., alias="periodenverbrauchVorhersage", title="Periodenverbrauchvorhersage"
    )
    zeitreihentyp: str | None = Field(default="Z21", title="Zeitreihentyp")
    kunden_wert: Decimal | None = Field(..., alias="kundenWert", title="Kundenwert")
    grundzustaendiger: bool | None = Field(default=True, title="Grundzustaendiger")
    zaehlpunkt_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    einheitVorhersage: Mengeneinheit = Field(Mengeneinheit.KWH)
    einheitKunde: Mengeneinheit | None = Field(None)
