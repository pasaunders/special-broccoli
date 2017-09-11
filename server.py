from flask import Flask, render_template, request, flash
import re

app = Flask(__name__)
app.secret_key = 'supersecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def form():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if len(email) > 0 and len(first_name) > 0 and len(last_name) > 0 and len(password) > 8 and confirm_password == password and str.isalpha(first_name) and str.isalpha(last_name) and EMAIL_REGEX.match(email):
        flash('Thanks for submitting your information')
    else:
        if not len(email) > 0:
            flash('fill out the email field')
        if not len(first_name) > 0:
            flash('fill out the first name field')
        if not len(last_name) > 0:
            flash('fill out the last name field')
        if not len(password) > 8:
            flash('password too short')
        if not confirm_password == password:
            flash('password fields do not match')
        if not str.isalpha(first_name) or str.isalpha(last_name):
            flash('name fields may only contain alphabet letters')
        if not EMAIL_REGEX.match(email):
            flash('email field not valid')
    return render_template('display.html')


app.run(debug=True)
