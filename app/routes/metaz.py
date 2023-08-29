from flask import url_for
from flask_restx import Namespace, Resource

from ..config import LoadProxyGateConfig

api = Namespace("Metaz", description="Application metadata endpoints")


@api.route("")
class Metaz(Resource):
    def get(self):
        print(LoadProxyGateConfig().config)
        meta = {
            "version": LoadProxyGateConfig()("app_version"),
            "app_name": LoadProxyGateConfig()("app_name"),
            "google_auth": {
                "client_id": "621835299065-l26di2j94qnpfa20385uv08bq03gbk6j.apps.googleusercontent.com",
                "session_endpoint": url_for("app_routes_auth_google.get_session"),
            },
            "plex_auth": {
                "session_endpoint": url_for("app_routes_auth_plex.get_session"),
            },
        }
        return meta, 200
