import os

from flask import Blueprint, url_for
from flask_restx import Api, Resource

blueprint = Blueprint(__name__.replace(".", "_"), __name__)
api = Api(blueprint)


@api.route("")
class Metaz(Resource):
    def get(self):
        meta = {
            "version": os.environ["PROXY_GATE_VERSION"],
            "app_name": "Proxy Gate",
            "google_auth": {
                "client_id": "",
                "session_endpoint": url_for("app_routes_auth_google.get_session"),
            },
            "plex_auth": {
                "session_endpoint": url_for("app_routes_auth_plex.get_session"),
            },
        }
        return meta, 200
