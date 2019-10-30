import os
from flask_restful import Resource, fields, marshal_with
from project.apps.database.database import Database
from project.config.config import DATABASES_ROOT_DIRECTORY as DB_ROOT

get_response_description = {
    'name': fields.String,
    'directory': fields.String,
    'tables': fields.List(fields.String)
}


# TODO: TOO MANY USE-CASES ARE NOT ALLOWED AT THIS BETA-VERSION
# How to use: create only if not exists, delete if only exists
class DatabaseResource(Resource):

    # Get all databases names in databases root
    @marshal_with(get_response_description)
    def get(self, database):
        db = Database.restore(os.sep.join([DB_ROOT, database, database + '.dbconfig']))
        tables = [file[:-6] for root, dirs, files in os.walk(db.root) for file in files if file.endswith('.table')]
        return {
            'name': db.name,
            'directory': db.root,
            'tables': tables
        }

    def post(self, database):
        Database.create(database)
        return 'Created ' + database

    def delete(self, database):
        db = Database.restore(os.sep.join([DB_ROOT, database, database + '.dbconfig']))
        db.deleteFromStorage()
        return 'Deleted ' + database
