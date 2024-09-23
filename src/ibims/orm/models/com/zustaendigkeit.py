import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.themengebiet import Themengebiet
from ibims.orm.models.many import PersonzustaendigkeitenLink, ZustaendigkeitzusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.person import Person
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Zustaendigkeit(SQLModel, table=True):
    """
    Enthält die zeitliche Zuordnung eines Ansprechpartners zu Abteilungen und Zuständigkeiten.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zustaendigkeit.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zustaendigkeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Zustaendigkeit.json>`_
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
    abteilung: str | None = Field(default=None, title="Abteilung")
    """
    Berufliche Rolle des Ansprechpartners/ der Person
    """
    position: str | None = Field(default=None, title="Position")
    """
    Berufliche Rolle des Ansprechpartners/ der Person
    """
    zustaendigkeit_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    person_zustaendigkeiten_link: List["Person"] = Relationship(
        back_populates="zustaendigkeiten", link_model=PersonzustaendigkeitenLink
    )
    themengebiet: Themengebiet | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="zustaendigkeit_zusatzattribute_link",
        link_model=ZustaendigkeitzusatzAttributeLink,
    )
