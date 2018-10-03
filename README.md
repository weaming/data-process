# Data Process

Make processing 2d data more convenient

## Install

    pip install data-process

## Module description

* collect_csv_data: Collect data in a directory contains CSV files
* date: Generate current date and time; get the range of and start, end day of a period date; convert bettween string and `datetime.datetime` type
* date_range: Get the range of date from the start, end, range gap you provided
* decimal_helper: Convert float to Decimal type
* dict_helper: Replace the keys of a dict; infinite `defaultdict` data structure; get data by a series of keys
* filter_date: Filter a series date string by the given start, end date
* green_dict: Make the `dict` compatibal with the `json.dumps`, especially for `date(time)` type
* group_by: Group a series of `dict` by a list of functions; degroup a deep grouped dict by the depths
* io_csv: Read, write csv files
* io_json: Read, write json files
* io_files: List files in a glob pattern directories
* io_lines: Read as lines from a file except the lines are blank or start with '#'
* iter_dict: Convert dict for output, handled by the type of values separately
* join: Left, right, inner, outer join a series of dict as like in SQL
* list_helper: Flat a nested list
* pandas_helper: Functions wrapper for using `pandas` conveniently. Convert `pandas.DataFrame` to a list of dict; aggregate DataFrame by a field.
