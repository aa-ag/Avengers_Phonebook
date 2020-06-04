from avengers_phonebook import app, db, Message, mail
from flask import render_template, request, redirect, url_for
from avengers_phonebook.forms import PhoneNumberInfo, LoginForm
from avengers_phonebook.models import User, check_password_hash
from flask_login import login_required,login_user,current_user,logout_user

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/phonebook.html')
def phonebook():
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

@app.route('/register', methods=['GET','POST'])
def register():
    form = PhoneNumberInfo()
    if request.method == 'POST' and form.validate():
        usernamephone_number = form.usernamephone_number.data
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n", usernamephone_number, username, password, email)
        user = User(username, usernamephone_number, email, password)
        
        db.session.add(user)
        db.session.commit()
        
        msg = Message(f'Welcome! {email}', recipients=[email])
        msg.body =('Congrats on signing up!')
        msg.html = ('<h1> Welcome to Call An Avenger! </h1>' '<p> This will be fun! </p>')
        mail.send(msg)
    return render_template('register.html',form = form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html',form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))