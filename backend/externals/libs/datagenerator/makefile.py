import os
import csv
from .datagen import DataGenerator

from pathlib import Path

class FileManager:
    def __init__(self, filename):
        
        #DIRECTORY PATH HERE
        # self.path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + "/Tables/"
        self.path = str(Path(os.path.abspath(__file__)).parent.parent.parent.parent.parent) + '/Tables/'
        
        self.filename = filename

        try:
            os.makedirs(self.path)
        except FileExistsError:
            pass

        print("Saving data in: ", self.path+filename+".csv")

        self.file = open(self.path+filename+".csv", 'w', newline="")
        self.writer = csv.writer(self.file)
        self.headers = None
        self.types = None
        self.params = None
        self.size = None
        self.reset_marker = 0
        
    def set_values(self, headers, types, params, size):
        self.headers = headers
        self.types = types
        self.params = params
        self.size = size
        self.DG = DataGenerator(types, params, size)
    
    def change_rows(self, size):
        self.size = size
        self.DG.change_size(size)

    def reset_outliers(self):
        if not self.reset_marker:
            self.DG.reset_outliers()
            self.reset_marker = 1

    def write_headers(self):
        self.writer.writerow(self.headers)

    def write(self):
        self.writer.writerows(self.DG.count())

    # PRINT WIP #############    

    def close_file(self):
        self.file.close()
    
    def out_file(self):
        with open(self.path+self.filename+".csv", 'r', newline="") as f:
            return f.read()