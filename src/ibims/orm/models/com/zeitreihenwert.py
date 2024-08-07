import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.messwertstatus import Messwertstatus
from ibims.orm.models.enum.messwertstatuszusatz import Messwertstatuszusatz
from ibims.orm.models.many import LastgangwerteLink, ZeitreihenwertzusatzAttributeLink, ZeitreihewerteLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.lastgang import Lastgang
    from ibims.orm.models.bo.zeitreihe import Zeitreihe
    from ibims.orm.models.com.zeitspanne import Zeitspanne
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Zeitreihenwert(SQLModel, table=True):
    """
    Abbildung eines Zeitreihenwertes bestehend aus Zeitraum, Wert und Statusinformationen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitreihenwert.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitreihenwert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Zeitreihenwert.json>`_
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
    wert: float | None = Field(default=None, title="Wert")
    """
    Zeitespanne für das Messintervall
    """
    zeitreihenwert_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    lastgang_werte_link: List["Lastgang"] = Relationship(back_populates="werte", link_model=LastgangwerteLink)
    zeitreihe_werte_link: List["Zeitreihe"] = Relationship(back_populates="werte", link_model=ZeitreihewerteLink)
    status: Messwertstatus | None = Field(None)
    statuszusatz: Messwertstatuszusatz | None = Field(None)
    zeitspanne_id: uuid_pkg.UUID | None = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            ForeignKey("zeitspanne.zeitspanne_sqlid", ondelete="SET NULL"),
        )
    )
    zeitspanne: "Zeitspanne" = Relationship(
        back_populates="zeitreihenwert_zeitspanne",
        sa_relationship_kwargs={"foreign_keys": "[Zeitreihenwert.zeitspanne_id]"},
    )
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="zeitreihenwert_zusatzattribute_link",
        link_model=ZeitreihenwertzusatzAttributeLink,
    )
