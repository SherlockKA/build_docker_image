import redis

from flask_sqlalchemy import SQLAlchemy
from rq import Queue

# Create singletons
db = SQLAlchemy()
task_queue = Queue(connection=redis.Redis())
