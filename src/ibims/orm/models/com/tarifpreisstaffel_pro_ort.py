import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import TarifpreispositionProOrtpreisstaffelnLink, TarifpreisstaffelProOrtzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.tarifpreisposition_pro_ort import TarifpreispositionProOrt
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class TarifpreisstaffelProOrt(SQLModel, table=True):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. raw:: html

        <object data="../_static/images/bo4e/com/TarifpreisstaffelProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `TarifpreisstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/TarifpreisstaffelProOrt.json>`_
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
    arbeitspreis: float | None = Field(default=None, title="Arbeitspreis")
    """
    Der Arbeitspreis in ct/kWh
    """
    arbeitspreis_nt: float | None = Field(default=None, alias="arbeitspreisNT", title="Arbeitspreisnt")
    """
    Der Arbeitspreis für Verbräuche in der Niedertarifzeit in ct/kWh
    """
    grundpreis: float | None = Field(default=None, title="Grundpreis")
    """
    Der Grundpreis in Euro/Jahr
    """
    staffelgrenze_bis: float | None = Field(default=None, alias="staffelgrenzeBis", title="Staffelgrenzebis")
    """
    Oberer Wert, bis zu dem die Staffel gilt (exklusive)
    """
    staffelgrenze_von: float | None = Field(default=None, alias="staffelgrenzeVon", title="Staffelgrenzevon")
    """
    Unterer Wert, ab dem die Staffel gilt (inklusive)
    """
    tarifpreisstaffelproort_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    tarifpreispositionproort_preisstaffeln_link: List["TarifpreispositionProOrt"] = Relationship(
        back_populates="preisstaffeln",
        link_model=TarifpreispositionProOrtpreisstaffelnLink,
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="tarifpreisstaffelproort_zusatzattribute_link",
        link_model=TarifpreisstaffelProOrtzusatzAttributeLink,
    )
