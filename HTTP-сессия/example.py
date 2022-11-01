from flask import Flask

# callable WSGI-приложение
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Skypro!'


@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users():
    return 'Users', 302