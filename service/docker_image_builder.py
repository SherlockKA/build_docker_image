from flask import Flask
from flask_restful import Api
from service.handlers.build_docker import BuildDocker
from service.handlers.get_status import GetStatus
from service.handlers.update_db import UpdateDB
from service.handlers.get_docker_registry_link import GetDockerRegistryLink
from service.extensions import db


def docker_image_builder() -> None:
    """Create application factory.
    """

    # Init app
    service_app = Flask(__name__.split(".")[0])

    # Set db
    service_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(service_app)
    with service_app.app_context():
        db.create_all()

    # Set APIs
    api = Api(service_app)
    api.add_resource(BuildDocker, "/buildDocker")
    api.add_resource(GetStatus, "/getStatus")
    api.add_resource(GetDockerRegistryLink, "/getDockerRegistryLink")
    api.add_resource(UpdateDB, "/updateDB")
    return service_app
    
    
 
