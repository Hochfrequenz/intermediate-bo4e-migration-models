import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import (
    AufAbschlagProOrtstaffelnLink,
    AufAbschlagProOrtzusatzAttributeLink,
    AufAbschlagRegionalbetraegeLink,
)

if TYPE_CHECKING:
    from ibims.orm.models.com.auf_abschlag_regional import AufAbschlagRegional
    from ibims.orm.models.com.auf_abschlagstaffel_pro_ort import AufAbschlagstaffelProOrt
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class AufAbschlagProOrt(SQLModel, table=True):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang
    mit örtlichen Gültigkeiten abgebildet werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/AufAbschlagProOrt.json>`_
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
    netznr: str | None = Field(default=None, title="Netznr")
    """
    Die ene't-Netznummer des Netzes in dem der Aufschlag gilt.
    """
    ort: str | None = Field(default=None, title="Ort")
    """
    Der Ort für den der Aufschlag gilt.
    """
    postleitzahl: str | None = Field(default=None, title="Postleitzahl")
    """
    Die Postleitzahl des Ortes für den der Aufschlag gilt.
    """
    aufabschlagproort_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    staffeln: List["AufAbschlagstaffelProOrt"] = Relationship(
        back_populates="aufabschlagproort_staffeln_link",
        link_model=AufAbschlagProOrtstaffelnLink,
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="aufabschlagproort_zusatzattribute_link",
        link_model=AufAbschlagProOrtzusatzAttributeLink,
    )
    aufabschlagregional_betraege_link: List["AufAbschlagRegional"] = Relationship(
        back_populates="betraege", link_model=AufAbschlagRegionalbetraegeLink
    )
