from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class TransaktionsdatenQuantities(BaseModel):
    """
    This class adds additional data to the transaktionsdaten, which is needed for an energy amount
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    migration_id: str | None = Field(default=None, title="Migration_id")
    dokumentennummer: str = Field(..., title="Dokumentennummer")
    kategorie: str = Field(..., title="Kategorie")
    nachrichtenfunktion: str = Field(..., title="Nachrichtenfunktion")
    typ: str = Field(..., title="Typ")
    datumsformat: str = Field(..., title="Datumsformat")
    status: Any = Field(..., title="Status")
