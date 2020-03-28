import time
import csv

from .makefile import FileManager as fm
import datetime as dt
#import takeinput


def mainf(filename, headers, types, params, rows=None, time_start=None, time_end=None, period=None, chunk_size=10000):
    ### CREATES FILE AND GENERATES DATA

    csvfile  = fm(filename)
    if rows is None:
        rows, start, period = time_to_rows(time_start, time_end, period)
        headers.insert(0, "Time")
        types.insert("daterow")
        params.insert([start, period]) # rethink?
        csvfile.set_values(headers, types, params, chunk_size)
        csvfile.write_headers()
        for _ in range(rows//chunk_size):
            csvfile.write()
        csvfile.reset_rows(rows%chunk_size)
        csvfile.write()
        csvfile.close_file()
    else:
        csvfile.set_values(headers, types, params, chunk_size)
        csvfile.write_headers()
        for _ in range(rows//chunk_size):
            csvfile.write()
        csvfile.reset_rows(rows%chunk_size)
        csvfile.write()
        csvfile.close_file()

    return csvfile

def time_to_rows(start_str, end_str, period):
    """
    ex: 
    start_str = "2020-03-24 23:00:05" 
    end_str = "2019-03-25 23:00:00" 
    period = "0 1 30 0" #day, hr, min, sec  
    start_str < end_str 

    inputs are strings, output rows is int, output start and period are datetime objects
    """
    start = None
    end = None
    if (len(start_str.split()) > 1):
        start = dt.datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
        end = dt.datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
    else:
        start = dt.date.fromisoformat(start_str)
        end = dt.date.fromisoformat(end_str)
            
    li = list(map(int , period.split()))
    period = dt.timedelta(days=li[0], hours=li[1], minutes=li[2], seconds=li[3])

    rows = int(abs(end-start)/period)
    return (rows, start, period)


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