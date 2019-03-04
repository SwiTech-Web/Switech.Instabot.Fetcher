from plugins.sqlite_connection import SqliteConnection


def update_data_sqlite(rows):
    sqlite_connection = SqliteConnection()
    sqlite_connection.init_database()
    count = 0
    commit = False
    for row in rows:
        count += 1
        if count == len(rows) or count == 300:
            commit = True
            count = 0
        sqlite_connection.record_row(row, commit)
    sqlite_connection.close_connection()
    return
