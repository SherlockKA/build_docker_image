from service.extensions import db

class DockerBuildStorage(db.Model):
    # Define schema
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    docker_registry_link = db.Column(db.String(), default='')
    status = db.Column(db.String(), default='Building')
