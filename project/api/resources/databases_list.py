import os
from flask_restful import Resource, fields, marshal_with_field
from project.config.config import DATABASES_ROOT_DIRECTORY as DB_ROOT
from project.connector.database_connector import DatabaseConnector


class DatabasesListResource(Resource):

    # Get all databases names in databases root
    @marshal_with_field(fields.List(fields.String))
    def get(self):
        connector = DatabaseConnector()
        dbList = connector.getDatabasesList()
        connector.close()
        return dbList
