from flask import abort

from typing import Dict
from flask_restful import Resource, reqparse
from service.extensions import db
from service.tables.docker_build_storage import DockerBuildStorage



class UpdateDB(Resource):
    # Set args structure
    args = reqparse.RequestParser()
    args.add_argument("build_id", type=int, required=True)
    args.add_argument("docker_registry_link")
    args.add_argument("status")

    def post(self) -> Dict[str, str]:

        # Parse args
        args = self.args.parse_args()

        # Query db
        row = DockerBuildStorage.query.filter_by(id=args["build_id"]).first()	

        if row is None:
            abort(404)

        # Update db
        if "docker_registry_link" in args:
            row.docker_registry_link = args["docker_registry_link"]

        # Update db
        if "status" in args:
            row.status = args["status"]

        db.session.commit()
        
        return {'Result': 'Updated'}