from os import getenv
from dotenv import load_dotenv

from sqlmodel import create_engine

load_dotenv()

database_url = getenv("DATABASE_URL")

engine = create_engine(database_url, echo=True)

