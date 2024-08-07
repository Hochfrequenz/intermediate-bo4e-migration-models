import uuid as uuid_pkg
from typing import Any

from pydantic import ConfigDict
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.quantities_status import QuantitiesStatus
from ibims.orm.models.enum.sparte import Sparte
from ibims.orm.models.enum.typ import Typ


class TransaktionsdatenQuantities(SQLModel, table=True):
    """
    This class adds additional data to the transaktionsdaten, which is needed for an energy amount
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    migration_id: str | None = Field(default=None, title="Migration_id")
    import_fuer_storno_adhoc: str | None = Field(default=None, title="Import_fuer_storno_adhoc")
    pruefidentifikator: str | None = Field(default=None, title="Pruefidentifikator")
    datenaustauschreferenz: str | None = Field(default=None, title="Datenaustauschreferenz")
    nachrichtendatum: str | None = Field(default=None, title="Nachrichtendatum")
    nachrichten_referenznummer: str | None = Field(default=None, title="Nachrichten_referenznummer")
    absender: str | None = Field(default=None, title="Absender")
    empfaenger: str | None = Field(default=None, title="Empfaenger")
    dokumentennummer: str | None = Field(default=None, title="Dokumentennummer")
    kategorie: str | None = Field(default=None, title="Kategorie")
    nachrichtenfunktion: str | None = Field(default=None, title="Nachrichtenfunktion")
    trans_typ: str | None = Field(default=None, title="TransTyp")
    datumsformat: str | None = Field(default=None, title="Datumsformat")
    transaktionsdatenquantities_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    typ: Typ = Field(Typ.TRANSAKTIONSDATENQUANTITIES)
    sparte: Sparte = Field(None)
    status: QuantitiesStatus = Field(QuantitiesStatus.VALID)
