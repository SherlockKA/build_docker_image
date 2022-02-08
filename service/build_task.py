import docker
import io
import requests


def build_task(build_id: int, docker_file: bytes) -> None:
	"""This script tried to build the docker image and updates the db after.
	"""

	# Try build docker image
	try:
		client = docker.from_env()
		# Build Image
		image, _ = client.images.build(fileobj=io.BytesIO(docker_file))

		# Update cells from db
		requests.post('http://127.0.0.1:5000/updateDB',
						data= {"build_id": build_id,
								"docker_registry_link": image.id,
								"status": "Successful"})
	except:
		# Update cells from db
		requests.post('http://127.0.0.1:5000/updateDB',
				data= {"build_id": build_id,
						"status": "Failed"})