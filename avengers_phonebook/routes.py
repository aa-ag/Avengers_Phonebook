from avengers_phonebook import app
from flask import render_template, request

from avengers_phonebook.forms import AvengerInfo

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/phonebook.html')
def phonebook():
    # names = [('Captain America': '111-111-1111'), ('Iron Man': '222-222-2222'), ('Hulk': '333-333-3333'), ('Thor': '444-444-4444'), ('Black Widow': '555-555-5555'), ('Ms. Marvel': '666-666-6666'), ('Black Panthern': '777-777-7777'), ('Ant-Man': '888-888-8888'), ('Doctor Strange': '999-999-9999')]
    names = {
        'Captain Marvel:': 18001234455,
        'Captain America:': 5555555555,
        'Iron Man:': 6302227878,
        'Hulk:': 9990001111,
        'Black Widow:': 2304448899,
        'Thor:': 7792301718,
        'Black Panthern:': 1111111111,
        'Ant Man:': 9999999999
    }
    return render_template('phonebook.html', names = names)

@app.route('/newnum.html', methods=['GET', 'POST'])
def newnum():
    form = AvengerInfo()
    if request.method == 'POST' and form.validate():
        hero_name = form.hero_name.data
        legal_nam = form.legal_name.data
        skills = form.skills.data
        num = form.num.data
        print("\n", hero_name, legal_nam, skills, num)
    return render_template('newnum.html', form = form)