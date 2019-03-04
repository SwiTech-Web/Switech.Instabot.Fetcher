import mysql.connector

from plugins.config import CONFIGURATION


class MysqlConnection:
    def __init__(self):
        mysql_connection = mysql.connector.connect(
            user=CONFIGURATION.config['Username'],
            password=CONFIGURATION.config['Password'],
            database=CONFIGURATION.config['Database'],
            host=CONFIGURATION.config['Host']
        )
        self.connection = mysql_connection

    def get_all_users(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM table")
            result = cursor.fetchall()
        return result

    def close_connection(self):
        self.connection.close()
        return
