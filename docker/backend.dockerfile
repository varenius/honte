FROM python:3.8.2-buster
RUN pip install pipenv

RUN mkdir -p /backend
COPY Pipfile Pipfile.* /backend/
WORKDIR /backend
RUN pipenv install --system

CMD python manage.py migrate && python manage.py runserver 0:8000
