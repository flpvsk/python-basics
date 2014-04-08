import os
import json
import logging
from datetime import date


__all__ = ('with_data_dumping', )

BASE_DIR = "dumps"
FILE_NAME_FORMAT = "{}-{}.json"
DEFAULT_FILE_NAME_FORMAT = "dump-{}.json"
DATE_FORMAT = "%y%m%d"


logging.basicConfig(filename='converter.log', level=logging.INFO)


def with_data_dumping(f):
    LOG = logging.getLogger('DumpFunction')

    def executor(*args, **kwargs):
        full_path = get_dump_file_full_path(args[1])
        if os.path.exists(full_path):
            with open(full_path) as dump_file:
                LOG.info("Loading data from dump file {}".format(full_path))
                return json.load(dump_file)
        else:
            if not os.path.exists(BASE_DIR):
                os.makedirs(BASE_DIR)
            data = f(*args, **kwargs)
            try:
                with open(full_path, 'w+') as dump_file:
                    dump_file.write(str(data).replace('\'', '\"'))
            except BaseException as e:
                LOG.warning("Data dump to file failed. Exception: {}".
                                                                 format(e))
            else:
                LOG.info("Data was saved to file {}".format(full_path))

        return data

    return executor


def get_dump_file_full_path(prefix):
    today_date = date.today().strftime(DATE_FORMAT)
    try:
        file_name = FILE_NAME_FORMAT.format(prefix, today_date)
    except:
        file_name = DEFAULT_FILE_NAME_FORMAT.format(today_date)
    return os.path.join(BASE_DIR, file_name)
