from flask_restx import Namespace, Resource, fields

ns = Namespace("Healthz", description="Application health realated endpoints")


class Models:
    Healthz = ns.model(
        "Healthz",
        {
            "status": fields.String(
                example="healthy",
                description="Overall application health status",
                enum=["healthy", "error"],
            ),
        },
        strict=True,
    )


@ns.route("")
class Healthz(Resource):
    @ns.marshal_with(Models.Healthz, description="Application health status")
    def get(self):
        return {"status": "healthy"}, 200
