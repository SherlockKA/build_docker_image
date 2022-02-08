build_docker_image:
		python3 client/client_request.py

service_up:
		rq worker & python3 main.py 

