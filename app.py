from flask import Flask, render_template

#referencing this file
app = Flask(__name__)

#Creating the index route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    #If there is any error,
    #it will show on the page
    app.run(debug=True)
