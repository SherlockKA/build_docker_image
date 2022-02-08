from service.docker_image_builder import docker_image_builder


if __name__ == "__main__":
    """This script runs the server.
    """

    # Create service app which builds docker images
    service_app = docker_image_builder()
    service_app.run()
    
 
