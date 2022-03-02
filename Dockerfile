FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /oc_p13_lettings
WORKDIR /oc_p13_lettings
COPY requirements.txt /oc_p13_lettings/
RUN pip install -r requirements.txt
COPY . /oc_p13_lettings/
CMD python3 manage.py runserver 0.0.0.0:8000