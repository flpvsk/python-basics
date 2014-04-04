import os
import json
from datetime import date


__all__ = ('dump_result_to_file', 'use_dump_data')

BASE_DIR = "dumps"
FILE_NAME_FORMAT = "{}-{}.json"
DEFAULT_FILE_NAME_FORMAT = "dump-{}.json"
DATE_FORMAT = "%y%m%d"


def use_dump_data(f):
    def executor(*args, **kwargs):
        full_path = get_dump_file_full_path(args[1])
        if not os.path.exists(full_path):
            return f()
        else:
            with open(full_path) as dump_file:
                #Should write to log with level 'INFO'
                print "Loading data from dump file {}".format(full_path)
                return json.load(dump_file)

    return executor


@use_dump_data
def dump_result_to_file(f):
    def executor(*args, **kwargs):
        if not os.path.exists(BASE_DIR):
            os.makedirs(BASE_DIR)
        data = f(*args, **kwargs)
        full_path = get_dump_file_full_path(args[1])
        if not os.path.exists(full_path):
            try:
                with open(full_path, 'w+') as dump_file:
                    dump_file.write(str(data).replace('\'', '\"'))
            except BaseException as e:
                #Should write to log with level 'WARNING'
                print "Data dump to file failed. Exception: {}".format(e)
            else:
                #Should write to log with level 'INFO'
                print "Data was saved to file {}".format(full_path)

        return data

    return executor


def get_dump_file_full_path(prefix):
    today_date = date.today().strftime(DATE_FORMAT)
    try:
        file_name = FILE_NAME_FORMAT.format(prefix, today_date)
    except:
        file_name = DEFAULT_FILE_NAME_FORMAT.format(today_date)
    return os.path.join(BASE_DIR, file_name)
