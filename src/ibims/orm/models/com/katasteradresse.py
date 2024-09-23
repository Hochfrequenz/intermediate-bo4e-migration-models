import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import KatasteradressezusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.marktlokation import Marktlokation
    from ibims.orm.models.bo.messlokation import Messlokation
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Katasteradresse(SQLModel, table=True):
    """
    Dient der Adressierung über die Liegenschafts-Information.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Katasteradresse.svg" type="image/svg+xml"></object>

    .. HINT::
        `Katasteradresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Katasteradresse.json>`_
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
    flurstueck: str | None = Field(default=None, title="Flurstueck")
    gemarkung_flur: str | None = Field(default=None, alias="gemarkungFlur", title="Gemarkungflur")
    katasteradresse_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    marktlokation_katasterinformation: List["Marktlokation"] = Relationship(
        back_populates="katasterinformation",
        sa_relationship_kwargs={
            "primaryjoin": "Marktlokation.katasterinformation_id==Katasteradresse.katasteradresse_sqlid",
            "lazy": "joined",
        },
    )
    messlokation_katasterinformation: List["Messlokation"] = Relationship(
        back_populates="katasterinformation",
        sa_relationship_kwargs={
            "primaryjoin": "Messlokation.katasterinformation_id==Katasteradresse.katasteradresse_sqlid",
            "lazy": "joined",
        },
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="katasteradresse_zusatzattribute_link",
        link_model=KatasteradressezusatzAttributeLink,
    )
