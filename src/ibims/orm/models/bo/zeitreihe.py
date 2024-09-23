import uuid as uuid_pkg
from typing import TYPE_CHECKING, List

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig

from ibims.orm.models.enum.medium import Medium
from ibims.orm.models.enum.mengeneinheit import Mengeneinheit
from ibims.orm.models.enum.messart import Messart
from ibims.orm.models.enum.messgroesse import Messgroesse
from ibims.orm.models.enum.typ import Typ
from ibims.orm.models.enum.wertermittlungsverfahren import Wertermittlungsverfahren
from ibims.orm.models.many import ZeitreihewerteLink, ZeitreihezusatzAttributeLink

if TYPE_CHECKING:
    from ibims.orm.models.com.zeitreihenwert import Zeitreihenwert
    from ibims.orm.models.zusatz_attribut import ZusatzAttribut


class Zeitreihe(SQLModel, table=True):
    """
    Abbildung einer allgemeinen Zeitreihe mit einem Wertvektor.
    Die Werte können mit wahlfreier zeitlicher Distanz im Vektor abgelegt sein.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zeitreihe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitreihe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/v202401.2.1/src/bo4e_schemas/bo/Zeitreihe.json>`_
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )
    id: str | None = Field(default=None, alias="_id", title=" Id")
    """
    Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    """
    beschreibung: str | None = Field(default=None, title="Beschreibung")
    """
    Beschreibt die Verwendung der Zeitreihe
    """
    bezeichnung: str | None = Field(default=None, title="Bezeichnung")
    """
    Bezeichnung für die Zeitreihe
    """
    version: str | None = Field(default=None, title="Version")
    """
    Version der Zeitreihe
    """
    zeitreihe_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    typ: Typ | None = Field(Typ.ZEITREIHE)
    einheit: Mengeneinheit | None = Field(None)
    medium: Medium | None = Field(None)
    messart: Messart | None = Field(None)
    messgroesse: Messgroesse | None = Field(None)
    werte: List["Zeitreihenwert"] = Relationship(back_populates="zeitreihe_werte_link", link_model=ZeitreihewerteLink)
    wertherkunft: Wertermittlungsverfahren | None = Field(None)
    zusatzAttribute: List["ZusatzAttribut"] = Relationship(
        back_populates="zeitreihe_zusatzattribute_link",
        link_model=ZeitreihezusatzAttributeLink,
    )
