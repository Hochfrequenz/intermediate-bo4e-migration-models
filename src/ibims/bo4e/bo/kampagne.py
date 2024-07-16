from pydantic import BaseModel, ConfigDict, Field

from ..enum.typ import Typ
from ..zusatz_attribut import ZusatzAttribut


class Kampagne(BaseModel):
    """
    A "Kampagne"/campaign models which marketing activities led customers to a product/tariff.
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
    )
    versionstruktur: str | None = Field(default="2", title="Versionstruktur")
    typ: Typ | None = Typ.GESCHAEFTSOBJEKT
    zusatz_attribute: list[ZusatzAttribut] | None = Field(
        default=None, alias="zusatzAttribute", title="ZusatzAttribute"
    )
    id: str = Field(..., title="Id")
    name: str = Field(..., title="Name")
