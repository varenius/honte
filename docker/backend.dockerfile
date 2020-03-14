FROM python:3.8.2-buster
RUN mkdir -p /honte/backend
COPY backend/Pipfile /honte/backend/Pipfile
COPY backend/Pipfile.lock /honte/backend/Pipfile.lock
WORKDIR /honte/backend
RUN pip install pipenv
RUN pipenv install --system
CMD python manage.py migrate && python manage.py runserver 0:8000
