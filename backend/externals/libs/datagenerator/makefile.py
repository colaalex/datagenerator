import os
import csv
from .datagen import DataGenerator

class FileManager:
    def __init__(self, filename):
        
        #DIRECTORY PATH HERE
        self.path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + "/Tables/"
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
        self.rows_per_iter = None 
        
    def set_values(self, headers, types, params, chunk_size):
        self.headers = headers
        self.types = types
        self.params = params
        self.chunk_size = chunk_size
        self.DG = DataGenerator(types, params, chunk_size)

    def write_headers(self):
        self.writer.writerow(self.headers)

    def write(self):
        self.writer.writerows(self.DG.count())

    # PRINT WIP #############    

    def close_file(self):
        self.file.close()