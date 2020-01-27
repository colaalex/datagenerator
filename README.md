# Datagenerator backend
Серверная часть веб-приложения. 

## Как запустить
Данный проект представляет собой docker-compose проект. Соответственно, для запуска необходимо иметь установленный [Docker](https://docs.docker.com/install/) и Docker-compose (на Windows и Mac идет вместе с докером, [инструкция для Linux](https://docs.docker.com/compose/install/))

Также перед первым запуском в директории `datagenerator` нужно создать файл `secret.py`, в котором будет всего одно поле `SECRET_KEY = '...'`. 

После установки необходимо перейти в директорию с проектом и ввести команду `docker-compose up`. При первом запуске будут загружены все необходимые зависимости.

Проверить работу приложения после запуска можно по адресу http://localhost:8000

## Методы API
**GET** `/api/generate`

Генерирует данные на основании переданных параметров. Параметры передаются вместе с GET-запросом, например `/api/generate?rows=30&header=test&header=pest&header=crest&type=normal&type=normal&type=triangular&params=[[0,12],[0,10],[5,10,15]]`

Список параметров:
* `rows` - количество строк (int)
* `header` - заголовок столбца, передается столько раз, сколько столбцов ожидается (string)
* `type` - тип распределения для отдельного столбца, передается столько раз, сколько столбцов ожидается (string)
* `params` - список параметров распределения, задается в виде списка (аналогичо json) (list)
---
### Типы распределений
* `beta(a: float, b: float)`
* `binomial(n: int >= 0, p: float >= 0)`
* `exponential(scale: float >= 0)`
* `gamma(k: float >= 0, theta: float >= 0)`
* `geometric(p: float >= 0)`
* `hypergeometric(ngood: int >= 0, nbad: int >= 0, nall: int 1<=nall<=ngood+nbad)`
* `laplace(mean: float, scale: float >=0)`
* `logistic(mean: float, scale: float >= 0)`
* `lognormal(mean: float, std: float >= 0)`
* `logarithmic(p: float 0<p<1)`
* `multinomial(n: int >= 0, pr_of_vals: list of float (sum of them must be 1))`
* `negative_binomial(n: int > 0, p: float 0<=p<=1)`
* `normal(mean: float, std: float >= 0)`
* `poisson(lam: float > 0)`
* `triangular(left: float, top: float >= left, right: float >= top)`
* `uniform(left: float, right: float > left)`
* `weibull(a: float >= 0)`