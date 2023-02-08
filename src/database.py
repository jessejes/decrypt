from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

_engine = create_engine("sqlite:///../credentials.db")
Base.metadata.create_all(bind=_engine)

_sessionmaker = sessionmaker(bind=_engine)
session = _sessionmaker()


