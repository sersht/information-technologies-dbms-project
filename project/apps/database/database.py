import os
import json
from shutil import rmtree
from pathlib import Path
from project.apps.table.table import Table


# TODO: Replace as import from controller
DATABASES_ROOT_DIRECTORY = os.sep.join(['C:', 'Projects', 'database'])


# Database essentially is a context for tables
class Database:

    @staticmethod
    def create(name):
        database = Database()
        database.name = name
        database.root = os.sep.join([DATABASES_ROOT_DIRECTORY, name])
        database.tables = {}

        if not Path(database.root).exists():
            os.makedirs(database.root)
        
        database.saveOnStorage()

        return database

    @staticmethod
    def restore(configPath):
        if not Path(configPath).is_file():
            raise ValueError('Given path is not a file')

        database = Database()

        with open(configPath, 'r') as file:
            database.__dict__ = json.load(file)

        database.tables = Database._restoreTables(database.root)

        return database

    @staticmethod
    def _restoreTables(root):
        tables = {}

        for file in os.listdir(root):
            if file.endswith(".table"):
                table = Table.restore(os.path.join(root, file))
                tables[table.name] = table
        
        return tables

    def saveOnStorage(self):
        for table in self.tables.values():
            table.saveOnStorage()
        
        delattr(self, 'tables')

        with open(os.sep.join([self.root, self.name + '.dbconfig']), 'w') as file:
            json.dump(self.__dict__, file, skipkeys=True)

        self.tables = {}

    def deleteFromStorage(self):
        # Recursively removes all directories-tree from the root
        rmtree(self.root)

    def addTable(self, name, columns, types):        
        if name in self.tables.keys():
            raise Exception('Table ' + "'" + name + "'" + ' already exists')
        
        self.tables[name] = Table.create(name, columns, types, self.root)

    def removeTable(self, name):
        if name not in self.tables.keys():
            raise Exception('Table ' + "'" + name + "'" + ' does not exist')

        self.tables.pop(name)
