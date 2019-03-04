import sqlite3

from plugins.config import CONFIGURATION


class SqliteConnection:
    def __init__(self):
        sqlite_connection = sqlite3.connect(CONFIGURATION.config['Target'] + "\\database.sqlite")
        self.connection = sqlite_connection

    def commit_change(self):
        self.connection.commit()
        return

    def init_database(self):
        with self.connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS users")
            cursor.execute("CREATE TABLE users(username, password, hashtag)")
            self.commit_change()
        return

    def record_row(self, row, commit=False):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO users VALUES ('{username}', '{password}', '{hashtag}')".format(
                username=row[0],
                password=row[1],
                hashtag=row[2]
            ))
        if commit:
            self.commit_change()
        return

    def close_connection(self):
        self.connection.close()
        return
