FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8

COPY . /app
RUN cd /app && python3 /app/setup_db.py