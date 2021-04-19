# AWS_Flask_CRUD_Web_Application

# Quick Start Using Pipenv

```
# Activate venv
$ pipenv shell

# Install dependencies
$ pipenv install

# Create DB
$ python
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py
```
# Endpoints
  * POST  /employee/add
  * GET   /employees
  * GET   /employee/getbyid/"id"
  * POST  /employee/update
  * POST  /employee/delete/"id"/
  * POST  /employee/salary/add
  * POST  /employees/salaries
  * GET   /employee/salary/getbyid/"id"
  * POST  /employee/salary/update
  * POST  /employee/salary/delete/"id"

# Postman Script
- Please find the postman script for all above REST endpoint [here](https://github.com/nilaynarlawar/AWS_Flask_CRUD_Web_Application/blob/main/Flask-AWS-Project.postman_collection.json)

# Docker Setup


# Github Actions


# AWS ECS deployment (CI/CD)

