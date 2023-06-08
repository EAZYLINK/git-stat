from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, select
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)

from config import db

Base = declarative_base()



class User(Base):
    __tablename__ = "user"
    email = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, primary_key=True)
    password = Column(String(50), nullable=False)

def __repr__(self):
    return "<User(email='%s', username='%s', password='%s')>"%(
        self.email, self.username, self.password)


new_user = User(email = 'eazy@example.com', username = 'eazy', password = 'Eazy1')
Session = db.connect_db()[0]
with Session.begin() as session:
    user = select(User)
    session.add(new_user)
    session.commit()

    
