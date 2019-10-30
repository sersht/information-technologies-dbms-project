import os
from flask_restful import Resource, fields, marshal_with
from project.apps.database.database import Database
from project.config.config import DATABASES_ROOT_DIRECTORY as DB_ROOT

get_response_description = {
    'columnTypes': fields.List(fields.String),
    'columnNames': fields.List(fields.String),
    'records': fields.List(fields.List(fields.String))
}


class TableResource(Resource):

    @marshal_with(get_response_description)
    def get(self, database, table):
        dbConfigPath = os.sep.join([DB_ROOT, database, database + '.dbconfig'])
        db = Database.restore(dbConfigPath)
        tbl = db.tables[table]
        return {
            'columnTypes': tbl.types,
            'columnNames': tbl.columns,
            'records': tbl.records
        }

    def post(self, database, table):
        pass

    def delete(self, database, table):
        db = Database.restore(os.sep.join([DB_ROOT, database]))
        db.removeTable(table)
        return 'Deleted ' + table + ' in ' + database

    def put(self, database, table):
        pass
