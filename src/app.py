from flask import Flask
from flask_cors import CORS
from routes.navigation import navigation
from routes.authentication import authentication
from routes.settings import settings
from routes.reports import reports
from elasticsearch import Elasticsearch


def create_app():
    app = Flask(__name__)

    CORS(app)

    elasticsearch_client = Elasticsearch(hosts=["http://elasticsearch:9200/"])
    app.elasticsearch_client = elasticsearch_client

    app.register_blueprint(navigation, url_prefix="/dvi-logging/navigation")
    app.register_blueprint(authentication, url_prefix="/dvi-logging/authentication")
    app.register_blueprint(settings, url_prefix="/dvi-logging/settings")
    app.register_blueprint(reports, url_prefix="/dvi-logging/reports")

    return app
    
    
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    