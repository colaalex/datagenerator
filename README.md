# Datagenerator 
Генератор данных и отчетов

## Как запустить
Данный проект представляет собой docker-compose проект. Соответственно, для запуска необходимо иметь установленный [Docker](https://docs.docker.com/install/) и Docker-compose (на Windows и Mac идет вместе с докером, [инструкция для Linux](https://docs.docker.com/compose/install/))

Также перед первым запуском в директории `datagenerator` нужно создать файл `secret.py`, в котором будут поля 
* `SECRET_KEY = '...'` - секретный ключ django-приложения;
* `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '...'` - Google Consumer Key;
* `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '...'` - Google Consumer Secret

Как получить Consumer Key см. инструкции на Google Cloud Console.

Затем в директории с кодом необходимо выполнить сборку проекта командой `docker-compose build`. При сборке будут загружены необходимые зависимости.

После установки необходимо перейти в директорию с проектом и ввести команду `docker-compose up`. 

Проверить работу приложения после запуска можно по адресу http://localhost:1337
