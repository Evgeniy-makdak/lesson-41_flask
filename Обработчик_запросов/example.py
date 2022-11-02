from flask import Flask, request

# callable WSGI-приложение
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    # Получить доступ к содержимому запроса можно через специальный объект request
    if request.method == 'POST':
        return 'Hello, POST!'
    return 'Hello, GET!'


@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users_post():
    return 'POST /users'


app.run(debug=True)
