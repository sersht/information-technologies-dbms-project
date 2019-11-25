from project.apps.table.table import Table
from project.connector.database_connector import DatabaseConnector


# Database essentially is a context for tables
class Database:

    @staticmethod
    def restoreFromDb(dbname):
        database = Database()
        database.name = dbname
        database.tables = Database._restoreTables(dbname)
        return database

    @staticmethod
    def _restoreTables(dbname):
        tables = {}
        con = DatabaseConnector()
        for tablename in con.getDatabaseTables(dbname):
            table = Table.restore(dbname, tablename)
            tables[table.name] = table
        con.close()
        return tables

    def saveOnDatabase(self):
        for table in self.tables.values():
            table.saveOnDatabase()

        con = DatabaseConnector()
        con.insertDatabaseToList(self.name)
        con.close()

    def deleteFromDatabase(self):
        con = DatabaseConnector()
        con.deleteAllTablesInDatabase(self.name)
        con.deleteDatabaseFromList(self.name)
        con.close()

    def addTable(self, name, columns, types):
        if name in self.tables.keys():
            raise Exception('Table ' + "'" + name + "'" + ' already exists')

        self.tables[name] = Table.create(name, self.name, columns, types)

    def removeTable(self, name):
        if name not in self.tables.keys():
            raise Exception('Table ' + "'" + name + "'" + ' does not exist')

        self.tables[name].deleteFromDatabase()
        self.tables.pop(name)
