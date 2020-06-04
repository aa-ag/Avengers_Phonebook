from avengers_phonebook import app, db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Avenger(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    hero_name = db.Column(db.String(100), nullable = False, unique = True)
    legal_name = db.Column(db.String(100), nullable = False, unique = False)
    skills = db.Column(db.String(250), nullable = False, unique = False)
    num = db.Column(db.String(10), nullable = False, unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.relationship('New Num', backref = 'by', lazy = True)

    def __init__(self, hero_name, legal_name, skills, num):
        self.hero_name = hero_name
        self.legal_name = legal_name
        self.skills = skills
        self.num = num

    def __repr__(self):
        return f"{self.hero_name}'s phone number has been added!"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    newnum = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f"{self.username} has been created with {self.email}"