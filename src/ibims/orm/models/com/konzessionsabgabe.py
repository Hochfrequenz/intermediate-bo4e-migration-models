import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.abgabe_art import AbgabeArt
from ibims.orm.models.many import KonzessionsabgabezusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.zaehlwerk import Zaehlwerk
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Konzessionsabgabe(SQLModel, table=True):
    """
    Diese Komponente wird zur Übertagung der Details zu einer Konzessionsabgabe verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Konzessionsabgabe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Konzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Konzessionsabgabe.json>`_
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
    kategorie: str | None = Field(default=None, title="Kategorie")
    """
    Gebührenkategorie der Konzessionsabgabe
    """
    kosten: float | None = Field(default=None, title="Kosten")
    """
    Konzessionsabgabe in E/kWh
    """
    konzessionsabgabe_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    satz: AbgabeArt | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="konzessionsabgabe_zusatzattribute_link",
        link_model=KonzessionsabgabezusatzAttributeLink,
    )
    zaehlwerk_konzessionsabgabe: List["Zaehlwerk"] = Relationship(
        back_populates="konzessionsabgabe",
        sa_relationship_kwargs={
            "primaryjoin": "Zaehlwerk.konzessionsabgabe_id==Konzessionsabgabe.konzessionsabgabe_sqlid",
            "lazy": "joined",
        },
    )
