from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///git-stat.db")
def connect_db():
    Session = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(bind=engine)
    return Session