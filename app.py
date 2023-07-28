## create a simple web application

from flask import Flask, render_template

# Create the app

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Home page</h1>"

@app.route('/welcome')
def welcome():
    return "<h2>Welcome to the flask tutorials</h2>"

@app.route('/index')
def index():
    return "Welcome to the index page" 

@app.route('/success/<int:score>')
def success(score):
    return "The person is passed and the score is: " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person is fail and the score is :" + str(score)

@app.route('/form',methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')


if __name__==("__main__"):
    app.run(debug=True)