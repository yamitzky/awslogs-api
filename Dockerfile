FROM python:3.6-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api:app"]
