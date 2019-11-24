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

    def insertDatabaseToList(self, dbname):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO dblist (dbname) VALUES (%s)", (dbname,))
            self.connection.commit()

    def deletDatabaseFromList(self, dbname):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM dblist WHERE dbname = %s", (dbname,))
            self.connection.commit()
