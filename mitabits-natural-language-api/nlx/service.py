from flask import Flask
from flask import Response
from flask import json
from flask import request
from flask_cors import CORS

from nlx.providers import DefaultServiceProvider


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('nlx.settings.Config')
    if test_config:
        app.config.update(test_config)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    svc = DefaultServiceProvider(resources_path=app.config['RESOURCES_PATH'])

    def generate_json_response(obj):
        return Response(json.dumps(obj, sort_keys=False, indent=2), mimetype='application/json')

    @app.route("/api/annotate/", methods=['POST'])
    def annotate():
        if not request.json:
            return generate_json_response({})

        text = request.json['text']
        doc = svc.nlp.process_text(text)
        return generate_json_response(doc.as_dict())

    @app.route('/api/kb/<object_class>/search', methods=['GET'])
    def search(object_class):
        search_query = request.args.get('q', "")
        results = svc.kb.search(object_class, search_query)
        results = [r.as_dict() for r in results]
        return generate_json_response(results)

    return app
