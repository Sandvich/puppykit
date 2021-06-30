FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8

COPY . /app
RUN cd /app && python3 /app/setup_db.py

# This takes the latest blog post and removes the first two lines, along with the last one.
# By doing this, when it is included in the front page we skip the navbar etc.
RUN sed '1d;2d;$d' /app/templates/blog/site_setup.html > /app/templates/latest_blog.html