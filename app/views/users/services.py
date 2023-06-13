import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)
from models.user import User
from config import connect_db
from sqlalchemy import or_, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Session = connect_db
session = Session()

def user_exist(email, username):
   user = session.query(User).filter(or_(User.email==email, User.username==username)).all()
   if len(user)!=0 or user==None:
      return True
   else:
      return False

def create_account(email, username, password_hash):
   new_user = User(email, username, password_hash)
   session.add(new_user)
   session.commit()
   session.flush()
   return new_user

def get_user_by_username(username):
   user = session.query(User).filter(User.username==username).first()
   return user

def update_user(user, email, username, password_hash):
   user.email = email
   user.username = username
   user.password_hash = password_hash
   session.commit()
   session.flush()
   return user

def delete_user(user):
   session.delete(user)
   session.commit()
   session.flush()
   return user


engine = create_engine("sqlite:///git-stat.db")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
