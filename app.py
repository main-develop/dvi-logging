from flask import Flask
from flask_cors import CORS
from routes.navigation_route import navigation
from routes.authentication_route import authentication


def create_app():
    app = Flask(__name__)
    app.register_blueprint(navigation, url_prefix="/dvi-logging/navigation")
    app.register_blueprint(authentication, url_prefix="/dvi-logging/authentication")

    CORS(app)

    return app
    
    
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    