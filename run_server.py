from flask import Flask
from flask_restful import Api
from project.api.resources.databases_list import DatabasesListResource
from project.api.resources.database import DatabaseResource
from project.api.resources.table import TableResource

app = Flask(__name__)
api = Api(app)

api.add_resource(DatabasesListResource, '/databases')
api.add_resource(DatabaseResource, '/databases/<string:database>')
api.add_resource(TableResource, '/databases/<string:database>/tables/<string:table>')

if __name__ == '__main__':
    app.run(debug=True)
