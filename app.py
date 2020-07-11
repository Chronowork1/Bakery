from flask import Flask, g, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy

#referencing this file
app = Flask(__name__)
#Set secret key to work with sessions
app.secret_key = 'Razzi'
#Telling app where database is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#Initialize database
db = SQLAlchemy(app)

#Create User class 
class User:
    #create def __init__ with id, username and password
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    #Return a representation so we can see it working
    #on the command lines, to make sure it works
    def __repr__(self):
        return f'<User: {self.username}>'

#Global variable that represents all the users
users = []
#Append users to this list
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Becca', password='secret'))

#check the session at the beginning of the request
@app.before_request
def before_request():
    g.user = None
    #check if user_id exist in th session
    if 'user_id' in session:
        #Finding the user
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

#Creating the index route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#Created a index route to login.
@app.route('/login', methods=['GET', 'POST'])

#If the request method is post in html
#Get the username from request form in html,
#Loop through the list and check if the user have the username and password
def login():
    if request.method == 'POST':
        #Anytime a user attempt to login, when login, it will remove session and create new session
        #Remove user_id
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        #The user will have a value if found anything
        if user and user.password == password:
            session['user_id'] = user.id
             #After login redirect to profile page
            return redirect(url_for('profile'))

        #If enter wrong username or password, return back to login
        return redirect(url_for('login'))

    return render_template('login.html')

#Created a index route to profile.
@app.route('/profile')
def profile():
    #If not login, redirect to login screen
    if not g.user:
        return redirect(url_for('login'))
        
    return render_template('profile.html')

if __name__ == "__main__":
    #If there is any error,
    #it will show on the page
    app.run(debug=True)
