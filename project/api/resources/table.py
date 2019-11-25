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

patchRequestParser = reqparse.RequestParser()
patchRequestParser.add_argument('action', location='json', required=True)
patchRequestParser.add_argument('index', type=int, location='json', required=True)
patchRequestParser.add_argument('column', location='json')
patchRequestParser.add_argument('value', location='json')
# --------

def deserializeValue(type, value):
    return DataConverter.deserializeFromString(value, type)


def deserializeValues(types, values):
    result = []
    for i in range(len(types)):
        result.append(deserializeValue(TYPE_BY_CODE[types[i]], values[i]))
    return result


class TableResource(Resource):

    @marshal_with(get_response_description)
    def get(self, database, table):
        db = Database.restoreFromDb(database)
        tbl = db.tables[table]
        return {
            'types': tbl.types,
            'columns': tbl.columns,
            'records': tbl.records
        }

    def post(self, database, table):
        postRequest = postRequestParser.parse_args()
        db = Database.restoreFromDb(database)

        db.addTable(table, postRequest['columns'], postRequest['types'])

        return 'Created {} table in {} database'.format(table, database)

    def delete(self, database, table):
        db = Database.restoreFromDb(database)
        db.removeTable(table)
        return 'Deleted {} table in {} database'.format(table, database)

    def put(self, database, table):
        putRequest = putRequestParser.parse_args()
        table_ = Database.restoreFromDb(database).tables[table]

        table_.insert(deserializeValues(table_.types, putRequest['values']), putRequest['index'])
        table_.saveOnDatabase()

        return 'Added new row in {} table in {} database'.format(table, database)

    def patch(self, database, table):
        patchRequest = patchRequestParser.parse_args()
        table_ = Database.restoreFromDb(database).tables[table]

        if patchRequest['action'] == 'update':
            typeIndex = table_.columns.index(patchRequest['column'])

            table_.update(
                patchRequest['index'],
                patchRequest['column'],
                deserializeValue(TYPE_BY_CODE[table_.types[typeIndex]], patchRequest['value'])
            )
            table_.saveOnDatabase()

            return 'Updated row {} in {} table in {} database'.format(patchRequest['index'], table, database)

        if patchRequest['action'] == 'delete':
            table_.delete(patchRequest['index'])
            table_.saveOnDatabase()

            return 'Deleted row {} in {} table in {} database'.format(patchRequest['index'], table, database)
