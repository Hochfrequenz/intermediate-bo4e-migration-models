import uuid as uuid_pkg
from datetime import datetime
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.many import ZeitspannezusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.zeitreihenwert import Zeitreihenwert
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Zeitspanne(SQLModel, table=True):
    """
    Eine Zeitspanne ist definiert aus Start und/oder Ende.
    Der Unterschied zur Menge (die auch zur Abbildung von Zeitmengen genutzt wird) ist, dass konkrete Start- und Endzeitpunkte angegeben werden.
    Die Zeitspanne ist aus dem COM Zeitraum hervorgegangen, das in Zeitspanne und Menge aufgeteilt wurde.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitspanne.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitspanne JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Zeitspanne.json>`_
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
    ende: datetime | None = Field(default=None, title="Ende")
    """
    inklusiver Beginn
    """
    start: datetime | None = Field(default=None, title="Start")
    """
    inklusiver Beginn
    """
    zeitspanne_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    zeitreihenwert_zeitspanne: List["Zeitreihenwert"] = Relationship(
        back_populates="zeitspanne",
        sa_relationship_kwargs={
            "primaryjoin": "Zeitreihenwert.zeitspanne_id==Zeitspanne.zeitspanne_sqlid",
            "lazy": "joined",
        },
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="zeitspanne_zusatzattribute_link",
        link_model=ZeitspannezusatzAttributeLink,
    )
