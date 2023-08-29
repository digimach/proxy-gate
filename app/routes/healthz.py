from flask_restx import Namespace, Resource

api = Namespace(
    "Healthz", description="Application health realated endpoints"
)


@api.route("")
class Healthz(Resource):
    def get(self):
        return "OK", 200
