FROM aandersonlins/back-python-dependences:latest

COPY . $APP_PATH
RUN python manage.py collectstatic --noinput -v 3

