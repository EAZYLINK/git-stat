from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)



Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    email = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, primary_key=True, unique=True)
    password_hash = Column(String(50), nullable=False)


    def __repr__(self):
        return "<User(email='%s', username='%s', password='%s')>"%(
            self.email, self.username, self.password_hash)

    def __init__(self, email, username, password_hash):
        self.email = email
        self.username = username
        self.password_hash = password_hash

engine = create_engine("sqlite:///git-stat.db")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
    
