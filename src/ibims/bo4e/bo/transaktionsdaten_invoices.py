from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class TransaktionsdatenInvoices(BaseModel):
    """
    This class adds additional data to the transaktionsdaten, which is needed for an invoice
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    lieferrichtung: str | None = Field(default=None, title="Lieferrichtung")
    referenznummer: str | None = Field(default=None, title="Referenznummer")
    duplikat: str = Field(..., title="Duplikat")
    status: Any = Field(..., title="Status")
