import os
from flask_restful import Resource, fields, marshal_with_field
from project.config.config import DATABASES_ROOT_DIRECTORY as DB_ROOT


class DatabasesListResource(Resource):

    # Get all databases names in databases root
    @marshal_with_field(fields.List(fields.String))
    def get(self):
        return [db for root, dirs, files in os.walk(DB_ROOT) for db in dirs]
