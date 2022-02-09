import base64

from typing import Dict
from flask_restful import Resource, reqparse
from service.extensions import db, task_queue
from service.tables.docker_build_storage import DockerBuildStorage
from service.build_task import build_task


class BuildDocker(Resource):
	# Set args structure
	args = reqparse.RequestParser()
	args.add_argument("docker_file", type=str, location='form', required=True)

	def post(self) -> Dict[str, str]:

		# Parse args
		args = self.args.parse_args()

		# Convert base64 string to byte array  
		docker_file = base64.b64decode(args["docker_file"])
		
		# Create empty row in db
		row = DockerBuildStorage()
		db.session.add(row)
		db.session.commit()

		# Put docker buld image task to Redis queue
		# Use row.id as build_id. Row.id is unique and generated automatically by db
		task_queue.enqueue(build_task, row.id, docker_file)
		
		return {'build_id': row.id}
    		
