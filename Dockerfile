FROM python:3.8-alpine
WORKDIR /
COPY Pipfile Pipfile
RUN pipenv shell
RUN pipenv install
RUN Create db
RUN exit()
EXPOSE 5000
COPY ./
CMD ["python","app.py"]
