from os import environ
from FlaskExercise import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5551'))
    except ValueError:
        PORT = 5551
    app.run(HOST, PORT, debug=True, ssl_context='adhoc')
