import os
from flask_restful import Resource, fields, marshal_with_field

# TODO: same hardcoded constant in database.py
DATABASES_ROOT_DIRECTORY = os.sep.join(['C:', 'Projects', 'database'])


class DatabasesListResource(Resource):

    # Get all databases names in databases root
    @marshal_with_field(fields.List(fields.String))
    def get(self):
        return [db for root, dirs, files in os.walk(DATABASES_ROOT_DIRECTORY) for db in dirs]
