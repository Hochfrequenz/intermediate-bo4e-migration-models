import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.landescode import Landescode
from ibims.orm.models.many import AdressezusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.bo.geschaeftspartner import Geschaeftspartner
    from ibims.orm.models.bo.marktlokation import Marktlokation
    from ibims.orm.models.bo.messlokation import Messlokation
    from ibims.orm.models.bo.person import Person
    from ibims.orm.models.com.ausschreibungsdetail import Ausschreibungsdetail
    from ibims.orm.models.com.vertragskonto_cba import VertragskontoCBA
    from ibims.orm.models.com.vertragskonto_mba import VertragskontoMBA
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Adresse(SQLModel, table=True):
    """
    Contains an address that can be used for most purposes.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Adresse.svg" type="image/svg+xml"></object>

    .. HINT::
        `Adresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/com/Adresse.json>`_
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
    adresszusatz: str | None = Field(default=None, title="Adresszusatz")
    """
    Zusatzhinweis zum Auffinden der Adresse, z.B. "3. Stock linke Wohnung"
    """
    co_ergaenzung: str | None = Field(default=None, alias="coErgaenzung", title="Coergaenzung")
    """
    Im Falle einer c/o-Adresse steht in diesem Attribut die Anrede. Z.B. "c/o Veronica Hauptmieterin"
    """
    hausnummer: str | None = Field(default=None, title="Hausnummer")
    """
    Hausnummer inkl. Zusatz; z.B. "3", "4a"
    """
    ort: str | None = Field(default=None, title="Ort")
    """
    Bezeichnung der Stadt; z.B. "Hückelhoven"
    """
    ortsteil: str | None = Field(default=None, title="Ortsteil")
    """
    Bezeichnung des Ortsteils; z.B. "Mitte"
    """
    postfach: str | None = Field(default=None, title="Postfach")
    """
    Im Falle einer Postfachadresse das Postfach; Damit werden Straße und Hausnummer nicht berücksichtigt
    """
    postleitzahl: str | None = Field(default=None, title="Postleitzahl")
    """
    Die Postleitzahl; z.B: "41836"
    """
    strasse: str | None = Field(default=None, title="Strasse")
    """
    Bezeichnung der Straße; z.B. "Weserstraße"
    """
    adresse_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    geschaeftspartner_adresse: List["Geschaeftspartner"] = Relationship(
        back_populates="adresse",
        sa_relationship_kwargs={
            "primaryjoin": "Geschaeftspartner.adresse_id==Adresse.adresse_sqlid",
            "lazy": "joined",
        },
    )
    marktlokation_lokationsadresse: List["Marktlokation"] = Relationship(
        back_populates="lokationsadresse",
        sa_relationship_kwargs={
            "primaryjoin": "Marktlokation.lokationsadresse_id==Adresse.adresse_sqlid",
            "lazy": "joined",
        },
    )
    messlokation_messadresse: List["Messlokation"] = Relationship(
        back_populates="messadresse",
        sa_relationship_kwargs={
            "primaryjoin": "Messlokation.messadresse_id==Adresse.adresse_sqlid",
            "lazy": "joined",
        },
    )
    person_adresse: List["Person"] = Relationship(
        back_populates="adresse",
        sa_relationship_kwargs={
            "primaryjoin": "Person.adresse_id==Adresse.adresse_sqlid",
            "lazy": "joined",
        },
    )
    landescode: Landescode | None = Field(Landescode.DE)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="adresse_zusatzattribute_link",
        link_model=AdressezusatzAttributeLink,
    )
    ausschreibungsdetail_marktlokationsadresse: List["Ausschreibungsdetail"] = Relationship(
        back_populates="marktlokationsadresse",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungsdetail.marktlokationsadresse_id==Adresse.adresse_sqlid",
            "lazy": "joined",
        },
    )
    ausschreibungsdetail_rechnungsadresse: List["Ausschreibungsdetail"] = Relationship(
        back_populates="rechnungsadresse",
        sa_relationship_kwargs={
            "primaryjoin": "Ausschreibungsdetail.rechnungsadresse_id==Adresse.adresse_sqlid",
            "lazy": "joined",
        },
    )
    vertragskontocba_vertragsAdresse: List["VertragskontoCBA"] = Relationship(
        back_populates="vertragsAdresse",
        sa_relationship_kwargs={
            "primaryjoin": "VertragskontoCBA.vertragsAdresse_id==Adresse.adresse_sqlid",
            "lazy": "joined",
        },
    )
    vertragskontomba_vertragsAdresse: List["VertragskontoMBA"] = Relationship(
        back_populates="vertragsAdresse",
        sa_relationship_kwargs={
            "primaryjoin": "VertragskontoMBA.vertragsAdresse_id==Adresse.adresse_sqlid",
            "lazy": "joined",
        },
    )
