import time
import csv

from .makefile import FileManager as fm
from . import takeinput


def mainf(filename, rows, headers, types, params, chunk_size):
    ### CREATES FILE AND GENERATES DATA
    start_time = time.time()

    csvfile = fm(filename)
    csvfile.set_values(headers, types, params, chunk_size)
    csvfile.write_headers()
    for i in range(rows//chunk_size):
        csvfile.write()
    csvfile.set_values(headers, types, params, rows%chunk_size)
    csvfile.write()
    csvfile.close_file()

    print("Time: ", time.time() - start_time)


if __name__ == '__main__':
    #rows = takeinput.take_number_of_records()
    #headers, types = takeinput.take_columns()
    #filename = takeinput.take_file_name()

    filename = "test"
    rows = 1000000
    size = 10000
    headers = ["name1", "name2", "name3", "1", "2", "3", "4", "out"]
    types = ["normal", "triangular", "beta", "classification"]
    params = [[0, 12], [5, 10, 15], [10, 20], [4, 2, 1, 3, ["f", "s", "t"]]]

    
    mainf(filename, rows, headers, types, params, size)