import uuid as uuid_pkg
from typing import Any

from pydantic import ConfigDict
from sqlmodel import Column, Field, PickleType, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.invoice_status import InvoiceStatus
from ibims.orm.models.enum.sparte import Sparte


class TransaktionsdatenInvoices(SQLModel, table=True):
    """
    This class adds additional data to the transaktionsdaten, which is needed for an invoice
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
    lieferrichtung: str | None = Field(default=None, title="Lieferrichtung")
    referenznummer: str | None = Field(default=None, title="Referenznummer")
    duplikat: str | None = Field(default=None, title="Duplikat")
    transaktionsdateninvoices_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    sparte: Sparte = Field(None)
    status: InvoiceStatus = Field(InvoiceStatus.ACCEPTED)
