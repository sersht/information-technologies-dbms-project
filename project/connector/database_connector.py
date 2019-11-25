import psycopg2


class DatabaseConnector:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='dbms-project',
            user='postgres',
            password='123456'
        )

    def close(self):
        self.connection.close()

    def getDatabasesList(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM dblist")
            dbList = cursor.fetchall()

        return dbList

    def insertDatabaseToList(self, dbname):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO dblist (dbname) VALUES (%s)", (dbname,))
            self.connection.commit()

    def deleteDatabaseFromList(self, dbname):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM dblist WHERE dbname = %s", (dbname,))
            self.connection.commit()

    def getDatabaseTables(self, dbname):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT DISTINCT tablename FROM databases WHERE dbname = %s", (dbname,))
            tablesList = cursor.fetchall()

        return tablesList

    def deleteAllTablesInDatabase(self, dbname):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM databases WHERE dbname = %s", (dbname,))
            self.connection.commit()

    def createTableInDatabase(self, dbname, tablename):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO databases (dbname, tablename, tabledata) VALUES (%s, %s, %s)",
                           (dbname, tablename, ""))
            self.connection.commit()

    def deleteTableInDatabase(self, dbname, tablename):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM databases WHERE dbname = %s AND tablename = %s", (dbname, tablename))
            self.connection.commit()

    def getTableInDatabase(self, dbname, tablename):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT tabledata FROM databases WHERE dbname = %s AND tablename = %s",
                           (dbname, tablename))
            self.connection.commit()
