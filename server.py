from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'supersecret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def form():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if not len(name) > 0 and len(comment) > 0 and len(comment) < 121:
        flash('invalid input - Name and comment fields must be filled out. Comment cannot exceed 120 characters.')
    return render_template('display.html', name=name, location=location, language=language, comment=comment)


app.run(debug=True)
