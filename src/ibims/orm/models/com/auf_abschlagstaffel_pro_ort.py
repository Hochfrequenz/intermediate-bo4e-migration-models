import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import AufAbschlagProOrtstaffelnLink, AufAbschlagstaffelProOrtzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.auf_abschlag_pro_ort import AufAbschlagProOrt
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class AufAbschlagstaffelProOrt(SQLModel, table=True):
    """
    Gibt den Wert eines Auf- oder Abschlags und dessen Staffelgrenzen an

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagstaffelProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/AufAbschlagstaffelProOrt.json>`_
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
    staffelgrenze_bis: float | None = Field(default=None, alias="staffelgrenzeBis", title="Staffelgrenzebis")
    """
    Oberer Wert, bis zu dem die Staffel gilt.
    """
    staffelgrenze_von: float | None = Field(default=None, alias="staffelgrenzeVon", title="Staffelgrenzevon")
    """
    Unterer Wert, ab dem die Staffel gilt.
    """
    wert: float | None = Field(default=None, title="Wert")
    """
    Der Wert für den Auf- oder Abschlag.
    """
    aufabschlagstaffelproort_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    aufabschlagproort_staffeln_link: List["AufAbschlagProOrt"] = Relationship(
        back_populates="staffeln", link_model=AufAbschlagProOrtstaffelnLink
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="aufabschlagstaffelproort_zusatzattribute_link",
        link_model=AufAbschlagstaffelProOrtzusatzAttributeLink,
    )
