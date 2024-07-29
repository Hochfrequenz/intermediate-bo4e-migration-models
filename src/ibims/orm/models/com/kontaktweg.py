import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.kontaktart import Kontaktart
from ibims.orm.models.many import GeschaeftspartnerkontaktwegeLink, KontaktwegzusatzAttributeLink, PersonkontaktwegeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.bo.person import Person
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Kontaktweg(SQLModel, table=True):
    """
    Die Komponente wird dazu verwendet, die Kontaktwege innerhalb des BOs Person darzustellen

    .. raw:: html

        <object data="../_static/images/bo4e/com/Kontakt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kontakt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Kontakt.json>`_
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
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    """
    Spezifikation, beispielsweise "Durchwahl", "Sammelnummer" etc.
    """
    ist_bevorzugter_kontaktweg: bool | None = Field(
        default=None, alias="istBevorzugterKontaktweg", title="Istbevorzugterkontaktweg"
    )
    """
    Gibt an, ob es sich um den bevorzugten Kontaktweg handelt.
    """
    kontaktwert: str | None = Field(default=None, title="Kontaktwert")
    """
    Die Nummer oder E-Mail-Adresse.
    """
    kontaktweg_sqlid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False
    )
    geschaeftspartner_kontaktwege_link: List["Geschaeftspartner"] = Relationship(
        back_populates="kontaktwege", link_model=GeschaeftspartnerkontaktwegeLink
    )
    person_kontaktwege_link: List["Person"] = Relationship(
        back_populates="kontaktwege", link_model=PersonkontaktwegeLink
    )
    kontaktart: Kontaktart | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="kontaktweg_zusatzattribute_link",
        link_model=KontaktwegzusatzAttributeLink,
    )
