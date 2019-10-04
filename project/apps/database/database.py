from os import makedirs
from json import dump, load
from shutil import rmtree
from pathlib import Path

# Replace as import from manager
DATABASES_ROOT_DIRECTORY = 'C:\Projects\database\\'


class Database:

    @staticmethod
    def create(self, name):
        database = Database()
        database.name = name
        database.root = DATABASES_ROOT_DIRECTORY + name + '\\'
        database.tables = []

        makedirs(database.root)
        database.saveOnStorage()

        return database

    @staticmethod
    def restore(configPath):
        if not Path(configPath).is_file():
            raise ValueError('Given path is not a file')
        
        database = Database()

        with open(configPath, 'r') as file:
            database.__dict__ = load(file)
        
        return database

    def saveOnStorage(self):
        with open(self.root + 'config.txt', 'w') as file:
            dump(self.__dict__, file)

    def deleteFromStorage(self):
        # Recursively removes all directories-tree from the root
        rmtree(self.root)
