from flask import Flask
from routes import routes

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.register_blueprint(routes)
    app.run(debug=True)