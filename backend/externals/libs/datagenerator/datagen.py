from numpy import random as r
import numpy as np
from faker import Faker
from sklearn.datasets import make_classification, make_regression
import matplotlib.pyplot as plt

class DataGenerator():
    def __init__(self, types, params, size=1000):
        self.funcs = types
        self.args = params
        self.size = size
        self.ru = Faker('ru_RU')
        self.en = Faker('en_US')
    
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

    ### DISTRIBUTIONS ###
    def beta(self, a, b):
        '''
        Parameters:\n
        a: float. b: float.
        '''
        data = r.beta(a, b, self.size)
        plt.hist(data)
        plt.savefig('/code/static/img/plot.png')
        plt.clf()
        return data

    def binomial(self, n, p):
        '''
        Parameters:\n
        n: integer, >=0 . p: float, >=0.
        '''
        data = r.binomial(n, p, self.size)
        plt.hist(data)
        plt.savefig('/code/static/img/plot.png')
        plt.clf()
        return data

    def exponential(self, scale):
        '''
        Parameters:\n
        scale: float >=0.
        '''
        return r.exponential(scale, self.size)

    def gamma(self, k, theta):
        '''
        Parameters:\n
        k: float, >=0 . theta: float, >=0.
        '''
        data = r.gamma(k, theta, self.size)
        plt.hist(data)
        plt.savefig('/code/static/img/plot.png')
        plt.clf()
        return data

    def geometric(self, p):
        '''
        Parameters:\n
        p: float, >=0.
        '''
        return r.geometric(p, self.size)

    def hypergeometric(self, ngood, nbad, nall):
        '''Parameters:\n
        ngood: integer, >=0.\n
        nbad: integer, >=0.\n
        nall: integer, >=1 and <=ngood+nbad.
        '''
        return r.hypergeometric(ngood, nbad, nall, self.size)

    def laplace(self, mean, scale):
        '''Parameters:\n
        mean: float. scale: float, >=0.
        '''
        data = r.laplace(mean, scale, self.size)
        plt.hist(data)
        plt.savefig('/code/static/img/plot.png')
        plt.clf()
        return data

    def logistic(self, mean, scale):
        '''
        Parameters:\n
        mean: float. scale: float, >=0.
        '''
        data = r.logistic(mean, scale, self.size)
        plt.hist(data)
        plt.savefig('/code/static/img/plot.png')
        plt.clf()
        return data

    def lognormal(self, mean, std):
        '''
        Parameters:\n
        mean: float. std: float, >=0.
        '''
        data = r.lognormal(mean, std, self.size)
        plt.hist(data)
        plt.savefig('/code/static/img/plot.png')
        plt.clf()
        return data

    def logarithmic(self, p):
        '''
        Parameters:\n
        p: float, must be in range (0, 1).
        '''
        return r.logseries(p, self.size)

    def multinomial(self, n, pr_of_vals):
        '''
        Parameters:\n
        n: int, >=0.\n
        pr_of_vals: list of float probabilities, sum must be = 1.
        '''
        return r.multinomial(n, pr_of_vals, self.size)

    def negative_binomial(self, n, p):
        '''
        Parameters:\n
        n: int, >0. p: float in range [0, 1].
        '''
        data = r.negative_binomial(n, p, self.size)
        plt.hist(data)
        plt.savefig('/code/static/img/plot.png')
        plt.clf()
        return data

    def normal(self, mean, std):
        '''
        Parameters:\n
        mean: float. std: float >=0.
        '''
        data = r.normal(mean, std, self.size)
        plt.hist(data)
        plt.savefig('/code/static/img/plot.png')
        plt.clf()
        return data

    def poisson(self, lam):
        '''
        Parameters:\n
        lam: float, >0.
        '''
        return r.poisson(lam, self.size)

    def triangular(self, left, top, right):
        '''
        Parameters:\n
        left: float. \n
        top: float, must be >= left.\n
        right: float, must be >= top.
        '''
        return r.triangular(left, top, right, self.size)

    def uniform(self, left, right):
        '''
        Parameters:\n
        left: float.\n
        right: float, must be >left.
        '''
        data = r.uniform(left, right, self.size)
        plt.hist(data)
        plt.savefig('/code/static/img/plot.png')
        plt.clf()
        return data

    def weibull(self, a):
        '''
        Parameters:\n
        a: float, >=0.
        '''
        return r.weibull(a, self.size)

    ### ML-like DATA
    def classification(self, n_features, n_informative, n_redundant, n_classes, labels=0, weights=0, noise=0.01, complexity=1.0, intervals=0):
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
   
    def regression(self, n_features, n_informative, noise, bias, n_outliers):
        '''
        # n_infomative must be <= n_features \n
        # noise: float >=0. default: 0 \n
        # bias: float >=. default: 0
        '''
        #Generates X, y for regression problem
        X, y = make_regression(n_samples=self.size, n_features=n_features, n_informative=n_informative, noise=noise, bias=bias, shuffle=False)

        #Makes outliers using spherical coordinates
        X_distance_max = np.max(np.ptp(X)/2) #radius of n-dim sphere which includes all X data
        X_distances = r.random(n_outliers) * X_distance_max * 1.5
        alphas = r.random(n_outliers) * 2 * np.pi
        betas = r.random((n_outliers, n_features-2)) * np.pi
        angles = np.concatenate((np.array([alphas]).T, betas), axis=1)

        #Trasforms spherical coordinates into Euclidian
        li = []
        length = angles.shape[1]
        i = length
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
        y_outliers = (y_distance + (y_distance * r.random(n_outliers) * 2)) * r.choice((-1, 1), n_outliers) + bias
        
        #Adds outliers into existing data
        indices = r.choice(n_samples, n_outliers)
        y[indices] = y_outliers
        X[indices] = X_outliers

        #shuffle rows
        a = np.concatenate((X, np.array([y]).T), axis=1)
        r.shuffle(a)
        X = a[:, :-1]
        y = a[:, -1]

        return X.T, y

    #TEXT GENERATORS
    def address_ru(self):
        return [self.ru.address() for _ in range(self.size)]

    def address_en(self):
        return [self.en.address() for _ in range(self.size)]

    def name_ru(self):
        return [self.ru.name() for _ in range(self.size)]

    def name_en(self):
        return [self.en.name() for _ in range(self.size)]

    def random_word(self, words):
        '''words: list of strings'''
        return [self.ru.random_element(words) for _ in range(self.size)]

    def date(self, end_datetime=None):
        return [self.ru.date(pattern="%d-%m-%Y", end_datetime=end_datetime) for _ in range(self.size)]

    def time(self):
        return [self.ru.time(pattern='%H:%M:%S') for _ in range(self.size)]

    def location(self):
        return [(float(self.ru.latlng()[0]), float(self.ru.latlng()[1])) for _ in range(self.size)]

    def ip(self):
        return [self.ru.ipv4() for _ in range(self.size)]

    def isbn10(self):
        return [self.ru.isbn10() for _ in range(self.size)]

    def isbn13(self):
        return [self.ru.isbn13() for _ in range(self.size)]

    def password(self):
        return [self.ru.password() for _ in range(self.size)]

    def phone_number_ru(self):
        return [self.ru.phone_number() for _ in range(self.size)]

    def phone_number_en(self):
        return [self.en.phone_number() for _ in range(self.size)]

    def sentence_en(self, n_words):
        return [self.en.sentence(n_words) for _ in range(self.size)]

    def text_en(self, chars):
        return [self.en.text(chars) for _ in range(self.size)]

    def sentence_ru(self, n_words):
        return [self.ru.sentence(n_words) for _ in range(self.size)]

    def text_ru(self, chars):
        return [self.ru.text(chars) for _ in range(self.size)]
    

