import os
import time
import plugins.db_mysql as mysql
import plugins.db_export as export
import plugins.utils as utils

from plugins.PyLogger.pylogger import pylogger


os.chdir(os.path.dirname(os.path.realpath(__file__)))


def main():
    pylogger.info("Script Started")
    start = time.time()
    rows = mysql.fetch_data_from_repository()
    export.update_user_repository(rows[0])
    end = time.time()
    second_elapsed = round(end - start)
    time_elapsed = utils.second_to_format(second_elapsed)
    pylogger.info("Script Executed in {}".format(
        time_elapsed
    ))


if __name__ == '__main__':
    main()
