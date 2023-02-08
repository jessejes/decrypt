from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Credential(Base):
    __tablename__ = "credentials"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String)
    email = Column("email", String)
    password = Column("password", String)
    url = Column("url", String)
    comment = ("comment", String)
    
    def __init__(self, id, title, email, password, url, comment):
        self.id = id
        self.title = title
        self.email = email
        self.password = password
        self.url = url
        self.comment = comment

class RequestCredential():

    def __init__(self, title, email, password, url, comment):
        self.title = title
        self.email = email
        self.password = password
        self.url = url
        self.comment = comment
