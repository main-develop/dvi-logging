from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    CORS(app)

    return app
    
    
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)