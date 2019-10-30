import os
from flask_restful import Resource, fields, marshal_with, reqparse
from project.apps.database.database import Database
from project.config.config import DATABASES_ROOT_DIRECTORY as DB_ROOT
from project.apps.table.data_converter import DataConverter
from project.apps.table.customtypes.types_map import TYPE_BY_CODE

get_response_description = {
    'types': fields.List(fields.String),
    'columns': fields.List(fields.String),
    'records': fields.List(fields.List(fields.String))
}

# --------
# Fold/Remove this block into some readable form
postRequestParser = reqparse.RequestParser()
postRequestParser.add_argument('columns', action='append', location='json', required=True)
postRequestParser.add_argument('types', action='append', location='json', required=True)

putRequestParser = reqparse.RequestParser()
putRequestParser.add_argument('index', type=int, location='json')
putRequestParser.add_argument('values', action='append', location='json', required=True)
# --------

def deserializedValues(types, values):
    result = []
    for i in range(len(types)):
        result.append(DataConverter.deserializeFromString(values[i], TYPE_BY_CODE[types[i]]))
    return result

class TableResource(Resource):

    @marshal_with(get_response_description)
    def get(self, database, table):
        dbConfigPath = os.sep.join([DB_ROOT, database, database + '.dbconfig'])
        db = Database.restore(dbConfigPath)
        tbl = db.tables[table]
        return {
            'types': tbl.types,
            'columns': tbl.columns,
            'records': tbl.records
        }

    def post(self, database, table):
        postRequest = postRequestParser.parse_args()
        creatorDbConfig = os.sep.join([DB_ROOT, database, database + '.dbconfig'])
        db = Database.restore(creatorDbConfig)

        db.addTable(table, postRequest['columns'], postRequest['types'])

        return 'Created ' + table + ' in ' + database

    def delete(self, database, table):
        db = Database.restore(os.sep.join([DB_ROOT, database]))
        db.removeTable(table)
        return 'Deleted ' + table + ' in ' + database

    def put(self, database, table):
        putRequest = putRequestParser.parse_args()
        creatorDbConfig = os.sep.join([DB_ROOT, database, database + '.dbconfig'])
        table_ = Database.restore(creatorDbConfig).tables[table]

        table_.insert(deserializedValues(table_.types, putRequest['values']), putRequest['index'])
        table_.saveOnStorage()

        return 'Added new row in ' + table + ' in ' + database
