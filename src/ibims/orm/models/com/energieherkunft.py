import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.erzeugungsart import Erzeugungsart
from ibims.orm.models.many import EnergieherkunftzusatzAttributeLink, EnergiemixanteilLink

if TYPE_CHECKING:
    from ibims.orm.models.com.energiemix import Energiemix
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Energieherkunft(SQLModel, table=True):
    """
    Abbildung einer Energieherkunft

    .. raw:: html

        <object data="../_static/images/bo4e/com/Energieherkunft.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energieherkunft JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Energieherkunft.json>`_
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
    anteil_prozent: float | None = Field(default=None, alias="anteilProzent", title="Anteilprozent")
    """
    Prozentualer Anteil der jeweiligen Erzeugungsart.
    """
    energieherkunft_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    erzeugungsart: Erzeugungsart | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="energieherkunft_zusatzattribute_link",
        link_model=EnergieherkunftzusatzAttributeLink,
    )
    energiemix_anteil_link: List["Energiemix"] = Relationship(back_populates="anteil", link_model=EnergiemixanteilLink)
