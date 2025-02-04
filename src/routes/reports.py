from flask import Blueprint, current_app, send_file, jsonify
from datetime import datetime, timedelta
from elasticsearch_reports.reports_generation.pages_time_spent import generate_pages_time_spent_report
import logging

reports = Blueprint("reports", __name__)

index_name = "dvi-logging"


@reports.route("/generate-report/pages_time_spent")
def pages_time_spent_report():
    try:
        elasticsearch_client = current_app.elasticsearch_client

        query = {
            "query": {
                "bool": {
                    "must": [
                        { "match": { "document.data.event_type": "page_navigation" } }
                    ],
                    "filter": [
                        {
                            "range": {
                                "@timestamp": {
                                    "gte": (datetime.utcnow() - timedelta(days=1)).isoformat(),
                                    "lte": datetime.utcnow().isoformat()
                                }
                            }
                        }
                    ]
                }
            }, 
            "size": 1000 # Number of documents
        }

        response = elasticsearch_client.search(index=index_name, body=query)

        logs = [hit["_source"]["document"]["data"] for hit in response["hits"]["hits"]]

        report_path = generate_pages_time_spent_report(logs)

        return send_file(report_path, mimetype="image/png")
    except Exception as error:
        logging.error(f"An error ocurred while sending a report: {error}")

        return jsonify({"message": "An error ocurred while sending a report", "details": error}), 500
