from flask import Flask, send_from_directory, abort, render_template

app = Flask(__name__)

@app.route('/tutor-photo/<name>')
def tutor_photo(name):
    allowed = {'teacher1', 'teacher2', 'teacher3'}
    if name not in allowed:
        abort(404)
    return send_from_directory('static/img', f'{name}.jpg')

@app.route("/")
def index():
    return render_template("index.html")
