from plugins.mysql_connection import MysqlConnection


def fetch_data_from_repository():
    mysql_connection = MysqlConnection()
    rows = mysql_connection.get_all_users()
    mysql_connection.close_connection()
    return rows

