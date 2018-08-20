from data_process.io_csv import new_csv_reader, process_row_generator

path = 'test.csv'
outpath = 'test.out.csv'

print('test read')
with new_csv_reader(path) as csv:
    data = list(csv)

print(data)

print('test write')
process_row_generator(list(data[0]), iter(data), outpath)
