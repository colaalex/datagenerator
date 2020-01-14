import os
import csv
from .datagen import DataGenerator

class FileManager:
    def __init__(self, filename):
        
        #DIRECTORY PATH HERE
        self.path = os.path.dirname(os.path.abspath(__file__)) + "\\Tables\\"
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
        
    def set_values(self, headers, types, params):
        self.headers = headers
        self.types = types
        self.params = params
        self.DG = DataGenerator(types, params)

    def write_headers(self):
        self.writer.writerow(self.headers)

    ### WIP
    def write(self):
        self.writer.writerow(self.DG.count())

    # PRINT WIP #############    

    def close_file(self):
        self.file.close()