FROM jfloff/alpine-python

WORKDIR /api

COPY requirements.txt /api/

RUN apk add postgresql-dev

RUN pip install -r requirements.txt

COPY . /api/

EXPOSE 6969
CMD [ "python", "main.py" ]