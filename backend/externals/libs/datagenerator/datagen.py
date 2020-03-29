from numpy import random as r
import numpy as np
from faker import Faker
from sklearn.datasets import make_classification, make_regression
import matplotlib.pyplot as plt
import datetime as dt

class DataGenerator():
    def __init__(self, types, params, size=1000, time_start=None, time_end=None, period_str=None):
        self.funcs = types
        self.args = params
        self.size = size        
        self.time_marker = 0        
        self.curr_time = None
        self.period = None
        self.ru = Faker('ru_RU')
        self.en = Faker('en_US')
        self.std_value = 1

    def change_size(self, size):
        self.size = size
    
    def reset_outliers(self):
        for args_list in self.args:
            args_list[-1] = 0
    
    def count(self):
        list_of_ML = ["classification", "regression"]
        li = []
        for i in range(len(self.funcs)):
            if self.funcs[i] not in list_of_ML:
                li.append(eval( "self." + self.funcs[i] + "(*" + str(self.args[i]) + ")" ))
            else:
                x, y = eval( "self." + self.funcs[i] + "(*" + str(self.args[i]) + ")" )
                for values in x:
                    li.append(values)
                li.append(y)
        return np.array(li).T.tolist()

    ### DATE COLUMN ###
    def daterow(self, st_time, period, outliers_n=0):
        if self.curr_time is None:
            self.curr_time = st_time
        data = np.array([self.curr_time + period*i for i in range(self.size)])
        self.curr_time = self.curr_time + period * self.size
        return data

    ### GEO DATA ###
    def location(self, lat, long, radius=0.001):        
        return np.array([ (Faker.coordinate(center=lat, radius=radius), Faker.coordinate(center=long, radius=radius)) for _ in range(self.size) ])
        
    ### DISTRIBUTIONS ###
    def beta(self, a, b, outliers_n=0):
        '''
        Parameters:\n
        a: float. b: float.
        '''
        data = r.beta(a, b, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(0.8, 1, outliers_n)
            data[indices] = outliers
        return data

    def binomial(self, n, p, outliers_n=0):
        '''
        Parameters:\n
        n: integer, >=0 . p: float, >=0.
        '''
        data = r.binomial(n, p, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.binomial(n*2, p+(1-p)/2, outliers_n)
            data[indices] = outliers
        return data

    def exponential(self, scale, outliers_n=0):
        '''
        Parameters:\n
        scale: float >=0.
        '''
        data = r.exponential(scale, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(np.max(data), self.std_value, outliers_n)
            data[indices] = outliers
        return data

    def gamma(self, k, theta, outliers_n=0):
        '''
        Parameters:\n
        k: float, >=0 . theta: float, >=0.
        '''
        data = r.gamma(k, theta, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(np.max(data), self.std_value, outliers_n)
            data[indices] = outliers
        return data

    def geometric(self, p, outliers_n=0):
        '''
        Parameters:\n
        p: float, >=0.
        '''
        data = r.geometric(p, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(np.max(data), 1, outliers_n)
            f = lambda x: int(x)
            outliers = f(outliers)
            data[indices] = outliers
        return data

    def hypergeometric(self, ngood, nbad, nall, outliers_n=0):
        '''Parameters:\n
        ngood: integer, >=0.\n
        nbad: integer, >=0.\n
        nall: integer, >=1 and <=ngood+nbad.
        '''
        data = r.hypergeometric(ngood, nbad, nall, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(np.max(data)*1.5, 1, outliers_n)
            f = lambda x: int(x)
            outliers = f(outliers)
            data[indices] = outliers
        return data

    def laplace(self, mean, scale, outliers_n=0):
        '''Parameters:\n
        mean: float. scale: float, >=0.
        '''
        data = r.laplace(mean, scale, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(np.max(data), self.std_value, outliers_n)
            randmult = r.choice([1.5, -1.5], outliers_n)
            outliers *= randmult
            data[indices] = outliers
        return data

    def logistic(self, mean, scale, outliers_n=0):
        '''
        Parameters:\n
        mean: float. scale: float, >=0.
        '''
        data = r.logistic(mean, scale, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(np.max(data), self.std_value, outliers_n)
            randmult = r.choice([1, -1], outliers_n)
            outliers *= randmult
            data[indices] = outliers
        return data

    def lognormal(self, mean, std, outliers_n=0):
        '''
        Parameters:\n
        mean: float. std: float, >=0.
        '''
        data = r.lognormal(mean, std, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.lognormal(mean+mean/2, self.std_value, outliers_n)
            data[indices] = outliers
        return data

    # def logarithmic(self, p):
    #     '''
    #     Parameters:\n
    #     p: float, must be in range (0, 1).
    #     '''
    #     return r.logseries(p, self.size)

    # def multinomial(self, n, pr_of_vals):
    #     '''
    #     Parameters:\n
    #     n: int, >=0.\n
    #     pr_of_vals: list of float probabilities, sum must be = 1.
    #     '''
    #     return r.multinomial(n, pr_of_vals, self.size)

    def negative_binomial(self, n, p, outliers_n=0):
        '''
        Parameters:\n
        n: int, >0. p: float in range [0, 1].
        '''
        data = r.negative_binomial(n, p, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(np.max(data)*1.5, 1, outliers_n)
            f = lambda x: int(x)
            outliers = f(outliers)
            data[indices] = outliers
        return data

    def normal(self, mean, std, outliers_n=0):
        '''
        Parameters:\n
        mean: float. std: float >=0.
        '''
        data = r.normal(mean, std, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(np.max(data), self.std_value, outliers_n)
            randmult = r.choice([1.5, -1.5], outliers_n)
            outliers *= randmult
            data[indices] = outliers
        return data

    def poisson(self, lam, outliers_n=0):
        '''
        Parameters:\n
        lam: float, >0. 
        '''
        data = r.poisson(lam, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(np.max(data)*1.5, 1, outliers_n)
            f = lambda x: int(x)
            outliers = f(outliers)
            data[indices] = outliers
        return data

    def triangular(self, left, top, right, outliers_n=0):
        '''
        Parameters:\n
        left: float. \n
        top: float, must be >= left.\n
        right: float, must be >= top.
        '''
        data = r.triangular(left, top, right, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(np.max(data), self.std_value, outliers_n)
            randmult = r.choice([1.5, -1.5], outliers_n)
            outliers *= randmult
            data[indices] = outliers
        return data

    def uniform(self, left, right, outliers_n=0):
        '''
        Parameters:\n
        left: float.\n
        right: float, must be >left.
        '''
        data = r.uniform(left, right, self.size)
        if outliers_n > self.size:
            outliers_n = self.size
        if outliers_n > 0:
            indices = r.choice(np.arange(len(data)), outliers_n)
            outliers = r.normal(np.max(data), self.std_value, outliers_n)
            randmult = r.choice([1.5, -1.5], outliers_n)
            outliers *= randmult
            data[indices] = outliers
        return data

    # def weibull(self, a):
    #     '''
    #     Parameters:\n
    #     a: float, >=0.
    #     '''
    #     return r.weibull(a, self.size)

    ### ML-like DATA
    def classification(self, n_features, n_informative, n_redundant, n_classes, labels=0, weights=0, noise=0.01, complexity=1.0, intervals=0, n_outliers=0):
        '''
        n_classes * n_clusters_per_class must be smaller or equal 2 ** n_informative \n
        n_inf + n_red <= n_features \n
        labels: list of labels, length = n_classes \n
        weights: list, proportion of classes, length = n_classes, sum=1 \n
        noice: percent of wrong y's, must be >=0 and <1 \n
        complexity: float >=0.5, default=1.0. Bigger number means easier solving \n
        intervals: list of intervals of each feature
        '''
        #transforms intervals into shift and scale
        shift = []
        scale = []
        if intervals != 0:
            for interval in intervals:
                shift.append((interval[1] + interval[0]) / (interval[1] - interval[0]))
                scale.append((interval[1] - interval[0]) / 2)
        else:
            shift = 0
            scale = 1

        if weights == 0:
            weights = None
        else:
            pass
            
        X, y = make_classification(n_samples=self.size, n_features=n_features, n_informative=n_informative, n_redundant=n_redundant,
         n_classes=n_classes, n_clusters_per_class=1, weights=weights, flip_y=noise, class_sep=complexity, shift=shift, scale=scale, shuffle=False)
        
        #naming labels if needed
        if labels != 0:
            y = np.array(np.array(y, dtype=np.int32), dtype=str)
            for i in range(n_classes):                
                y[y == str(i)] = labels[i]                
                
        #shuffle rows
        a = np.concatenate((X, np.array([y]).T), axis=1)
        r.shuffle(a)
        if labels != 0:
            X = np.array(a[:, :-1], dtype=np.float64)
        else:
            X = a[:, :-1]
        y = a[:, -1]

        return X.T, y
   
    def regression(self, n_features, n_informative, noise=0, bias=0, n_outliers=0):
        '''
        # n_infomative must be <= n_features \n
        # noise: float >=0. default: 0 \n
        # bias: float >=. default: 0
        '''
        #Generates X, y for regression problem
        X, y = make_regression(n_samples=self.size, n_features=n_features, n_informative=n_informative, noise=noise, bias=bias, shuffle=False)

        #Makes outliers using spherical coordinates
        X_distance_max = np.max(np.ptp(X)/2) #radius of n-dim sphere which includes all X data
        X_distances = r.rand(n_outliers)  * X_distance_max * 1.5
        alphas = r.rand(n_outliers) * 2 * np.pi
        betas = r.rand((n_outliers, n_features-2)) * np.pi
        angles = np.concatenate((alphas.T, betas), axis=1)

        #Trasforms spherical coordinates into Euclidian
        li = []
        length = angles.shape[1]
        i = length
        coords = 1
        while i >= 0:
            if i > 0:
                coords *= np.prod(np.sin(angles[:,length-i:]), axis=1)
            if i < length:
                coords *= np.cos(angles[:,length-i-1])
            i -= 1
            li.append(coords)
        X_outliers = np.array(li).T
        
        #Makes ouliers for y
        y_distance = np.ptp(y)/2 
        y_outliers = (y_distance + (y_distance * r.rand(n_outliers) * 2)) * r.choice((-1, 1), n_outliers) + bias
        
        #Adds outliers into existing data
        indices = r.choice(self.size, n_outliers)
        y[indices] = y_outliers
        X[indices] = X_outliers

        #shuffle rows
        a = np.concatenate((X, np.array([y]).T), axis=1)
        r.shuffle(a)
        X = a[:, :-1]
        y = a[:, -1]

        return X.T, y
    

    ### TEXT GENERATORS
    def address_ru(self):
        return np.array([self.ru.address() for _ in range(self.size)])

    def address_en(self):
        return np.array([self.en.address() for _ in range(self.size)])

    def name_ru(self):
        return np.array([self.ru.name() for _ in range(self.size)])

    def name_en(self):
        return np.array([self.en.name() for _ in range(self.size)])

    def random_word(self, words):
        '''words: list of strings'''
        return np.array([self.ru.random_element(words) for _ in range(self.size)])

    def date(self, end_datetime=None):
        return np.array([self.ru.date(pattern="%d-%m-%Y", end_datetime=end_datetime) for _ in range(self.size)])

    def time(self):
        return np.array([self.ru.time(pattern='%H:%M:%S') for _ in range(self.size)])

    def ip(self):
        return np.array([self.ru.ipv4() for _ in range(self.size)])

    def isbn10(self):
        return np.array([self.ru.isbn10() for _ in range(self.size)])

    def isbn13(self):
        return np.array([self.ru.isbn13() for _ in range(self.size)])

    def password(self):
        return np.array([self.ru.password() for _ in range(self.size)])

    def phone_number_ru(self):
        return np.array([self.ru.phone_number() for _ in range(self.size)])

    def phone_number_en(self):
        return np.array([self.en.phone_number() for _ in range(self.size)])

    def sentence_en(self, n_words):
        return np.array([self.en.sentence(n_words) for _ in range(self.size)])

    def text_en(self, chars):
        return np.array([self.en.text(chars) for _ in range(self.size)])

    def sentence_ru(self, n_words):
        return np.array([self.ru.sentence(n_words) for _ in range(self.size)])

    def text_ru(self, chars):
        return np.array([self.ru.text(chars) for _ in range(self.size)])
