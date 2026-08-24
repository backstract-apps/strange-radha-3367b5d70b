
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if value in (None, ""):
        raise RuntimeError(f"Missing required database env var: {name}")
    return value



DATABASE_URL = URL.create(

    drivername='postgresql+psycopg2',

    username=_required_env("DATABASE_USERNAME"),
    password=_required_env("DATABASE_PASSWORD"),
    host=_required_env("DATABASE_HOST"),
    port=int(_required_env("DATABASE_PORT")),
    database=_required_env("DATABASE_NAME")
)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
