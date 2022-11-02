from flask import Flask

# callable WSGI-приложение
app = Flask(__name__)


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'


app.run()
