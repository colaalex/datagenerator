from numpy import random as r
from numpy import array as array

class DataGenerator():
    def __init__(self, types, params):
        self.funcs = types
        self.args = params
        self.size = 1
    
    def count(self):
        li = [] 
        for i in range(len(self.funcs)):
            li.append(eval( "self." + self.funcs[i] + "(*" + str(self.args[i]) + ")" )[0]) ###might rethink 0 index
        return li

    ### DISTRIBUTIONS ###
    def beta(self, a, b):
        '''
        Parameters:\n
        a: float. b: float.
        '''
        return r.beta(a, b, self.size)

    def triangular(self, left, top, right):
        '''
        Parameters:\n
        left: float. \n
        top: float, must be >= left.\n
        right: float, must be >= top.
        '''
        return r.triangular(left, top, right, self.size)

    def normal(self, mean, std):
        '''
        Parameters:\n
        mean: float. std: float.
        '''
        return r.normal(mean, std, self.size)

    

    ###WIP###

    

# print(DataGenerator.tri)