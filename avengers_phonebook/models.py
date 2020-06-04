from avengers_phonebook import app, db, login

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    usernamephone_number = db.Column(db.String(150), nullable = False, unique = True,default="")
    username = db.Column(db.String(150), nullable = True, unique = True,default="")
    email = db.Column(db.String(150), nullable = True, unique = True,default="")
    password = db.Column(db.String(256),nullable = True,default="")
    def __init__(self,usernamephone_number,username,email,password):
        self.usernamephone_number = usernamephone_number
        self.username = username
        self.email = email
        self.password = self.set_password(password)
    
    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.phone_number} was added.'