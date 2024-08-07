import uuid as uuid_pkg

from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel._compat import SQLModelConfig


class File(SQLModel, table=True):
    """
    This class represents a file that is stored in the database.
    """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )
    file_name_for_docstore: str | None = Field(default=None, title="File Name For Docstore")
    folder_name_for_docstore: str | None = Field(default=None, title="Folder Name For Docstore")
    file: bytes = Field(..., title="File")
    file_sqlid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
