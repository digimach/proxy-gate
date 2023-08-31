import os
from flask import url_for
from flask_restx import Namespace, Resource, fields

from ..config import LoadProxyGateConfig

ns = Namespace("Metaz", description="Application metadata endpoints")


class Models:
    MetazGoogleAuth = ns.model(
        "MetazGoogleAuth",
        {
            "session_endpoint": fields.String,
            "client_id": fields.String,
        },
        strict=True,
    )

    MetazPlexAuth = ns.model(
        "MetazPlexAuth",
        {
            "session_endpoint": fields.String,
        },
        strict=True,
    )

    Metaz = ns.model(
        "Metaz",
        {
            "app_name": fields.String(
                example="Proxy Gate", description="Name of the application instance"
            ),
            "version": fields.String(
                example="1.0.2", description="Version of the running application"
            ),
            "google_auth": fields.Nested(
                MetazGoogleAuth, description="Google authentication metadata"
            ),
            "plex_auth": fields.Nested(
                MetazPlexAuth, description="Plex authentication metadata"
            ),
        },
        strict=True,
    )


@ns.route("")
class Metaz(Resource):
    @ns.marshal_with(Models.Metaz, description="Application metadata")
    @ns.doc("Get application public metadata")
    def get(self):
        meta = {
            "app_name": LoadProxyGateConfig()("app_name"),
            "version": os.environ.get("PROXY_GATE_APP_VERSION", "unknown"),
            "google_auth": {
                "client_id": "621835299065-l26di2j94qnpfa20385uv08bq03gbk6j.apps.googleusercontent.com",
                "session_endpoint": url_for("Authentication_google_auth_session"),
            },
            "plex_auth": {
                "session_endpoint": url_for("Authentication_plex_auth_session"),
            },
        }
        return meta, 200
