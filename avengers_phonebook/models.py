from avengers_phonebook import app, db, login

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), nullable = True, unique = True, default="")
    email = db.Column(db.String(150), nullable = True, unique = True, default="")
    password = db.Column(db.String(256), nullable = True, default="")
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.email} was added.'

class AvengerNum(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    avenger_name = db.Column(db.String(200))
    phone_num = db.Column(db.String(10))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, avenger_name, phone_num, user_id):
        self.avenger_name = avenger_name
        self.phone_num = phone_num
        self.user_id = user_id

    def __repr__(self):
        return f"Contact {self.avenger_name} at {self.phone_num}."