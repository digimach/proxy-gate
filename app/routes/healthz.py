from flask import Blueprint
from flask_restx import Api, Resource

blueprint = Blueprint(__name__.replace(".", "_"), __name__)
api = Api(blueprint)


@api.route("")
class Healthz(Resource):
    def get(self):
        return "OK", 200
