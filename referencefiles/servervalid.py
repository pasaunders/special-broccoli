from flask import Flask, render_template, redirect, request, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'supersecret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['Post'])
def process():
    if len(request.form['name']) < 1:
        flash('Name cannot be empty!')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('invalid email')
    else:
        flash('success!')
    return redirect('/')


app.run(debug=True)
