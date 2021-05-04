FROM python:3.9-alpine
WORKDIR /
COPY Pipfile Pipfile
RUN pipenv shell
RUN pipenv install
RUN exit()
EXPOSE 5000
COPY . /
CMD ["python","app.py"]
