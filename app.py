from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, email_validator, EqualTo
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

#referencing this file
app = Flask(__name__)
#Set secret key to work with sessions
app.config['SECRET_KEY'] = 'Razzi'
#Telling app where database is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config.from_pyfile('config.cfg')

#Initialize database
Bootstrap(app)
db = SQLAlchemy(app)
mail = Mail(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#Object orieted User
class User(UserMixin, db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Object oriented LoginForm
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

#Object oriented registerForm
class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    confirm =  PasswordField('confirm', validators=[InputRequired(), EqualTo('password', message="Password must match")])

#Route to template
@app.route('/', methods=['GET', 'POST'])
#Define a function that renders the page index
def index():
    if request.method == 'POST':
        bread_list = request.form.getlist('bread')
        for food in range(len(bread_list)):
            print(bread_list[food])
        #bread = request.form['bread']
        #print(bread_list)
        #return render_template('bread.html', bread=bread)
        #msg = Message('Favorite Bread', recipients=['landoxie@gmail.com'])
        #msg.body = "Your favorite bread is "  + str(bread_list[food])
        #mail.send(msg)

    #return 'Message has been sent'
    return render_template('index.html')

#Route to login
@app.route('/login', methods=['GET', 'POST'])
#Define a function login that search database.db for username, if the username and password matches,
#the page redirect to profile
def login():
    #pass form to template
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('profile'))
        return '<h1>Invalid username or password</h1>'
    return render_template('login.html', form=form)

#Route to signup
@app.route('/signup', methods=['GET', 'POST'])
#Define a function signup that add a user username, password and email to database.db
def signup():
    form = RegisterForm()
    #Check and see if the form has been submittedand added into database.
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
    return render_template('signup.html', form=form)

#Route to profile
@app.route('/profile', methods=['GET', 'POST'])
#Login on login.html required for access
@login_required
#Define a function that return the page of profile
def profile():
    return render_template('profile.html', name=current_user.username, id=current_user.id)

#@app.route('/send', methods=['GET', 'POST'])
#def send():
    #if request.method == 'POST':
        #bread = request.form['bread']
        #print(request.form.getlist('bread'))
        #return render_template('bread.html', bread=bread)
    #return render_template('index.html')

#Route to logout
@app.route('/logout')
#Login required on page
@login_required
#Define a function logout that redirect the user back to the index page
def logout():
    logout_user()
    return redirect(url_for('index'))

#If there is an error this will show.
if __name__ == '__main__':
    app.run(debug=True)
