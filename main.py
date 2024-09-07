from flask import Flask
from routes import test

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.register_blueprint(test)
    app.run(debug=True)