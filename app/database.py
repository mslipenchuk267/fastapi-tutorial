from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

SQLALCHEMY_DATABASE_HOST = os.getenv("FASTAPITUT_POSTGRESQL_DB_HOST")
SQLALCHEMY_DATABASE_NAME = os.getenv("FASTAPITUT_POSTGRESQL_DB_NAME")
SQLALCHEMY_DATABASE_USER = os.getenv("FASTAPITUT_POSTGRESQL_DB_USER")
SQLALCHEMY_DATABASE_PASS = os.getenv("FASTAPITUT_POSTGRESQL_DB_PASS")

#SQLALCHEMY_DATABASE_URL = "postgresql://myuser:mypass@localhost/fastapitutdb"
SQLALCHEMY_DATABASE_URL = f"postgresql://{SQLALCHEMY_DATABASE_USER}:{SQLALCHEMY_DATABASE_PASS}@{SQLALCHEMY_DATABASE_HOST}/{SQLALCHEMY_DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
