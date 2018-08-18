"""
from data_process.io_csv import new_csv_reader, process_row_generator


def read_csv():
    with new_csv_reader('origin.csv') as reader:
        for row in reader:
            yield row  # ordered dict


process_row_generator(['a', 'b', 'c'], read_csv, 'new.csv')
"""

import io
import csv
import sys
import os
from contextlib import contextmanager

CSV_FORMAT_PARAMS = dict(
    delimiter=',',
    quotechar='"',
)


@contextmanager
def new_csv_writer(path, fields, csv_format=None):
    f = None
    try:
        if path is None:
            f = sys.stdout
        elif hasattr(path, 'write'):
            f = path
        else:
            f = io.open(path, 'w', newline='', encoding='utf-8')
        yv = csv.DictWriter(f, fieldnames=fields, **(csv_format or CSV_FORMAT_PARAMS))
        yv.writeheader()
        yield yv
    finally:
        f and f.close()


@contextmanager
def new_csv_reader(path, fields=None, csv_format=None):
    f = None
    try:
        if hasattr(path, 'read'):
            f = path
        else:
            f = io.open(path, 'r', encoding='utf-8')
        yield csv.DictReader(f, fieldnames=fields, **(csv_format or CSV_FORMAT_PARAMS))
    finally:
        f and f.close()


def _process_row(writer, row):
    writer.writerow(row)


def process_row_generator(fields, generator, output, process_row=_process_row):
    c = 0

    with new_csv_writer(output, fields) as writer:
        for row in generator:
            process_row(writer, row)
            c += 1

    return c


def merge_csv_list(file_path_list, fields=None, csv_format=None):
    """
    merge data in some csv list to one list

    :return: list of ordereddict
    """
    rv = []

    def _process_row(row):
        rv.append(row)

    for fp in file_path_list:
        if not os.path.exists(fp):
            raise Exception('file {} does not exist'.format(fp))
        with new_csv_reader(fp, fields=fields, csv_format=csv_format) as reader:
            for row in reader:
                _process_row(row)

    return rv

