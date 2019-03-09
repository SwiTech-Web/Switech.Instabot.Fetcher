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
        cursor = self.connection.cursor()
        cursor.execute("SELECT ps_insta, pwd_insta, hashtag FROM user")
        result = cursor.fetchall()
        cursor.close()
        return result

    def close_connection(self):
        self.connection.close()
        return
