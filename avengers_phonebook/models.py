from avengers_phonebook import app, db

class Avenger(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    hero_name = db.Column(db.String(100), nullable = False, unique = True)
    legal_name = db.Column(db.String(100), nullable = False, unique = False)
    skills = db.Column(db.String(250), nullable = False, unique = False)
    num = db.Column(db.String(10), nullable = False, unique = True)

    def __init__(self, hero_name, legal_name, skills, num):
        self.hero_name = hero_name
        self.legal_name = legal_name
        self.skills = skills
        self.num = num

    def __repr__(self):
        return f"{self.hero_name}'s phone number has been added!"