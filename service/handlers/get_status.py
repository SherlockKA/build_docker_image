from typing import Dict
from flask import abort
from flask_restful import Resource, reqparse
from service.tables.docker_build_storage import DockerBuildStorage


class GetStatus(Resource):
	    # Set args structure
		args = reqparse.RequestParser()
		args.add_argument("build_id", type=int, required=True)

		def get(self) -> Dict[str, str]:
			# Parse args
			args = self.args.parse_args()

       		# Query db
			row = DockerBuildStorage.query.filter_by(id=args["build_id"]).first()	

			if row is None:
					abort(404)
					
			return {'Status': row.status}
