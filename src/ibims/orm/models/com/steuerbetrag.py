import uuid as uuid_pkg
from decimal import Decimal
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.steuerkennzeichen import Steuerkennzeichen
from ibims.orm.models.enum.waehrungscode import Waehrungscode
from ibims.orm.models.many import RechnungsteuerbetraegeLink, SteuerbetragzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.rechnung import Rechnung
    from ibims.orm.models.com.rechnungsposition import Rechnungsposition
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Steuerbetrag(SQLModel, table=True):
    """
    Abbildung eines Steuerbetrages.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Steuerbetrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Steuerbetrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Steuerbetrag.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    zusatz_attribute: Optional[list["ZusatzAttribut"]] = None

    # pylint: disable=duplicate-code
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        extra="allow",
        # json_encoders is deprecated, but there is no easy-to-use alternative. The best way would be to create
        # an annotated version of Decimal, but you would have to use it everywhere in the pydantic models.
        # See this issue for more info: https://github.com/pydantic/pydantic/issues/6375
        json_encoders={Decimal: str},
    )
    """
    version: str | None = Field(default="v202401.2.1", alias="_version", title=" Version")
    """
    Version der BO-Struktur aka "fachliche Versionierung"
    """
    basiswert: float | None = Field(default=None, title="Basiswert")
    """
    Nettobetrag für den die Steuer berechnet wurde. Z.B. 100
    """
    steuerwert: float | None = Field(default=None, title="Steuerwert")
    """
    Aus dem Basiswert berechnete Steuer. Z.B. 19 (bei UST_19)
    """
    steuerwert_vorausgezahlt: Decimal | None = Field(
        default=None, alias="steuerwertVorausgezahlt", title="Steuerwertvorausgezahlt"
    )
    steuerbetrag_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    rechnung_steuerbetraege_link: List["Rechnung"] = Relationship(
        back_populates="steuerbetraege", link_model=RechnungsteuerbetraegeLink
    )
    rechnungsposition_teilsummeSteuer: List["Rechnungsposition"] = Relationship(
        back_populates="teilsummeSteuer",
        sa_relationship_kwargs={
            "primaryjoin": "Rechnungsposition.teilsummeSteuer_id==Steuerbetrag.steuerbetrag_sqlid",
            "lazy": "joined",
        },
    )
    steuerkennzeichen: Steuerkennzeichen | None = Field(None)
    waehrung: Waehrungscode | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="steuerbetrag_zusatzattribute_link",
        link_model=SteuerbetragzusatzAttributeLink,
    )
