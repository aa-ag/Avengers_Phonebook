from avengers_phonebook import app, db, Message, mail
from flask import render_template, request, redirect, url_for
from avengers_phonebook.forms import UserInfoForm, PostNum, LoginForm
from avengers_phonebook.models import User, AvengerNum, check_password_hash
from flask_login import login_required, login_user, current_user, logout_user

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/phonebook.html')
def phonebook():
    nums = AvengerNum.query.all()
    return render_template('phonebook.html', nums = nums)

@app.route('/submitnum', methods=['GET','POST'])
@login_required
def submitnum():
    num = PostNum()
    if request.method == 'POST' and num.validate():
        name = num.avenger_name.data
        phone = num.phone_num.data
        user_id = current_user.id
        print('\n', name, phone)
        num = AvengerNum(name, phone, user_id)

        db.session.add(num)

        db.session.commit()

        return redirect(url_for('phonebook'))
    return render_template('submitnum.html', num = num)

@app.route('/num_detail/<int:num_id>')
@login_required
def num_detail(num_id):
    num = AvengerNum.query.get_or_404(num_id)
    return render_template('num_detail.html', num = num)

@app.route('/num_detail/update/<int:num_id>', methods = ['GET', 'POST'])
@login_required
def num_update(num_id):
    nums = AvengerNum.query.get_or_404(num_id)
    update_contact = PostNum()

    if request.method == 'POST' and update_contact.validate():
        name = update_contact.avenger_name.data
        num = update_contact.phone_num.data
        user_id = current_user.id
        print(name, num, user_id)

        nums.name = name
        nums.num = num
        nums.user_id = user_id

        db.session.commit()
        return redirect(url_for('phonebook.html', num_id = num.id))
    return render_template('phonebook.html', update_num = update_num)

@app.route('/num_detail/delete/<int:num_id>', methods=['POST'])
@login_required
def post_delete(num_id):
    num = AvengerNum.query.get_or_404(num_id)
    db.session.delete(num)
    db.session.commit()
    return redirect(url_for('phonebook'))

@app.route('/register', methods=['GET','POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n", username, password, email)
        user = User(username, email, password)
        
        db.session.add(user)
        db.session.commit()
        
        msg = Message(f'Welcome! {email}', recipients=[email])
        msg.body =('Congrats on signing up!')
        msg.html = ('<h1> Welcome to Call An Avenger! </h1>' '<p> This will be fun! </p>')
        mail.send(msg)
    return render_template('register.html', form = form)

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