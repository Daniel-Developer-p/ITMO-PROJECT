from flask import (
    Flask,
    render_template,
    url_for
)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('List1.html')


@app.route('/register')
def register():
    return render_template('Registration.html')


@app.route('/log')
def login():
    return render_template('Login.html')


@app.route('/films')
def films():
    return render_template('Blog1 (films).html')


@app.route('/serials')
def serials1():
    return render_template('Blog1 (serials).html')


@app.route('/cartoons')
def cartoons():
    return render_template('Blog1 (multi).html')


if __name__ == '__main__':
    app.run()
