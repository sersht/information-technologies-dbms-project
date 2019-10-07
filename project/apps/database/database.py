import os
import json
from shutil import rmtree
from pathlib import Path
from ..table.table import Table


# TODO: Replace as import from controller
DATABASES_ROOT_DIRECTORY = 'C:\\Projects\\database\\'


# Database essentially is a context for tables
class Database:

    @staticmethod
    def create(name):
        database = Database()
        database.name = name
        database.root = DATABASES_ROOT_DIRECTORY + name + '\\'
        database.tables = []

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
        tables = []

        for file in os.listdir(root):
            if file.endswith(".table"):
                tables.append(Table.restore(os.path.join(root, file)))
        
        return tables

    def saveOnStorage(self):
        with open(self.root + 'config.txt', 'w') as file:
            json.dump(self.__dict__, file)
        
        # Надо сделать - при сохранении базы данных - сохранять состояние всех таблиц

    def deleteFromStorage(self):
        # Recursively removes all directories-tree from the root
        rmtree(self.root)
