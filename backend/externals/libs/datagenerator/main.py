import time
import csv

from .makefile import FileManager as fm
import datetime as dt
#import takeinput


def mainf(filename, headers, types, params, rows=None, time_start=None, time_end=None, period=None, chunk_size=10000):
    ### CREATES FILE AND GENERATES DATA

    csvfile  = fm(filename)
    if time_start is not None:
        rows, start, period = time_to_rows(time_start, time_end, period)
        headers.insert(0, "Time")
        types.insert(0, "daterow")
        params.insert(0, [start, period, 0])
        csvfile.set_values(headers, types, params, chunk_size)
        csvfile.write_headers()
        for _ in range(rows//chunk_size):
            csvfile.write()
            csvfile.reset_outliers
        csvfile.change_rows(rows%chunk_size)
        csvfile.write()
        csvfile.close_file()
    else:
        csvfile.set_values(headers, types, params, chunk_size)
        csvfile.write_headers()
        for _ in range(rows//chunk_size):
            csvfile.write()
            csvfile.reset_outliers
        csvfile.change_rows(rows%chunk_size)
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
    filename = "test"
    rows = 10000000
    chunk_size = 10000
    # headers = ["name1", "name2", "name3"]
    # types = ["normal", "triangular", "beta"]
    # params = [[0, 3, 5000], [5, 10, 15], [10, 20]]
    headers = ["NORM",]
    types = ["normal",]
    params = [[0, 3, 10000],]

    mainf(filename, headers, types, params, rows)