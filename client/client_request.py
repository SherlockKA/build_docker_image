import requests
import base64
import time
import ast


if __name__ == "__main__":

	""" This scipt contains test of the client requests
	
		Steps:
			- Request building image
			- Each 1 second check the status of the building
			- Output docker registry link (just image id in our case) iff status ~ 'Successful'
			- Output warning iff status ~ 'Failed'
	
	"""

	parse_request = lambda request: ast.literal_eval(request.text)

	# Load Dockerfile and convert into b64encode
	data = {'docker_file': base64.b64encode(open('Dockerfile','rb').read())}

	# Send {builDocker} request
	request_output = parse_request(requests.post('http://127.0.0.1:5000/buildDocker', data=data))
	
	assert 'build_id' in request_output, 'Server did not return build_id'
	# Retreive {buil_id} and use it to check the status of the image building 
	build_id = request_output['build_id']
	print(f"Building Id: {build_id}")

	while True:
		# Wait 1 second
		time.sleep(1)

		# Get building status by {build_id}
		request_output = parse_request(requests.get(f'http://127.0.0.1:5000/getStatus?build_id={build_id}'))

		assert 'Status' in request_output, 'Invalid request output from /getStatus'
		assert request_output['Status'] in ['Building', 'Successful', 'Failed'], 'Invald status'

		if request_output['Status'] == 'Successful':
			# Get docker registry link by {build_id}
			request_output = parse_request(requests.get(f'http://127.0.0.1:5000/getDockerRegistryLink?build_id={build_id}'))
			assert 'Link' in request_output, 'Invalid request output from /getDockerRegistryLink'
			print(request_output['Link'])
			break
			
		elif request_output['Status'] == 'Failed':
			print("Building docker image has been failed")
			break


	
