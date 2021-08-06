from app import app
from flask import render_template
from app.templates import RegisterForm

@app.route('/')
def index():
    name = 'Diamond'
    title = 'Coding Temple Intro to Flask'
    return render_template('home.html', name=name, title=title)

@app.route('/home', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print ('THE FORM IS VALID')
        username = form.username.data
        phone_number= form.phone_number.data
    return render_template('phone_book.html')

