import uuid as uuid_pkg
from enum import Enum

from sqlmodel import Field, Relationship
from sqlmodel._compat import SQLModelConfig


class Aggregationsverantwortung(str, Enum):
    """
    Aggregationsverantwortung describes who is responsible for aggregations. This enum is not part of the official
    bo4e standard, but is already implemented in the c# and go versions:
    https://github.com/Hochfrequenz/BO4E-dotnet/blob/9bdc151170ddba5c9d7535e863d5a396fe7fec52/BO4E/ENUM/Aggregationsverantwortung.cs#L8
    https://github.com/Hochfrequenz/go-bo4e/blob/708b39de0dcea8a9448ed4e7341a2687f6bf7c11/enum/aggregationsverantwortung/aggregationsverantwortung.go
    """

    UENB = "UENB"
    VNB = "VNB"
