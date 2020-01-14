import time
import csv

from .makefile import FileManager as fm
from . import takeinput


def mainf(rows, headers, types, params, filename):
    ### CREATES FILE AND GENERATES DATA
    start_time = time.time()

    csvfile = fm(filename)
    csvfile.set_values(headers, types, params)
    csvfile.write_headers()
    for i in range(rows):
        csvfile.write()
    csvfile.close_file()

    print("Time: ", time.time() - start_time)


# if __name__ == '__main__':
#     #rows = takeinput.take_number_of_records()
#     #headers, types = takeinput.take_columns()
#     #filename = takeinput.take_file_name()

#     rows = 200000
#     headers = ["name1", "name2", "name3"]
#     types = ["normal", "triangular", "beta"]
#     params = [[0, 12], [5, 10, 15], [10, 20]]
#     filename = "test"
#     mainf(rows, headers, types, params, filename)