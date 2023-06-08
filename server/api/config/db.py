from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def connect_db():
    enginge = create_engine("sqlite:///git-stat", echo=True)
    Session = sessionmaker(bind=enginge)
    return [Session, enginge]