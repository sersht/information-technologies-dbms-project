import os
from flask_restful import Resource, fields, marshal_with
from project.apps.database.database import Database
from project.config.config import DATABASES_ROOT_DIRECTORY as DB_ROOT
from project.connector.database_connector import DatabaseConnector

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
        con = DatabaseConnector()
        tables = con.getDatabaseTables(database)
        con.close()
        return {
            'name': database,
            'directory': "---",
            'tables': tables
        }

    def post(self, database):
        con = DatabaseConnector()
        con.insertDatabaseToList(database)
        con.close()
        return 'Created ' + database

    def delete(self, database):
        db = Database.restoreFromDb(database)
        db.deleteFromDatabase()
        return 'Deleted ' + database
