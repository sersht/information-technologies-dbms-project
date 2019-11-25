import os
import json
from shutil import rmtree
from pathlib import Path
from project.apps.table.table import Table
from project.config.config import DATABASES_ROOT_DIRECTORY as DB_ROOT


# Database essentially is a context for tables
class Database:

    @staticmethod
    def restoreFromDb(dbname):
        database = Database()
        database.tables = Database._restoreTables(dbname)
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

        self.tables[name].deleteFromStorage()
        self.tables.pop(name)
