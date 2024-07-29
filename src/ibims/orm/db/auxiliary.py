"""
Auxiliary module to load url from env file
"""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


def get_url(dir: Optional[Path]) -> str:
    """
    Build the database connection URL based on the environment variables in .env
    """
    if dir is not None:
        load_dotenv(dotenv_path=dir / ".env")
    else:
        load_dotenv()

    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    server = os.getenv("POSTGRES_SERVER")
    port = os.getenv("POSTGRES_PORT")
    database = os.getenv("POSTGRES_DB")
    if user is None and password is None and server is None and database is None and port is None:
        raise IOError("Could not load .env file.")
    if user is None or password is None or server is None or database is None or port is None:
        raise KeyError(
            f"Couldn't find all environment variables:\n"
            f"\tuser: '{user}'\n"
            f"\tpassword: '{password}'\n"
            f"\tserver: '{server}'\n"
            f"\tport: '{port}'\n"
            f"\tdb: '{database}'"
        )
    return f"postgresql+psycopg://{user}:{password}@{server}:{port}/{database}"
