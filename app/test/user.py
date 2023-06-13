import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)
from config import connect_db
from models.user import User

Session = connect_db
session = Session()


def delete_user():
    new_user = session.query(User).delete(User.username=='eazy1')
    session.commit()
    session.flush()
    print(new_user)