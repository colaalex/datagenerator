FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /code
RUN mkdir /code/static
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/
