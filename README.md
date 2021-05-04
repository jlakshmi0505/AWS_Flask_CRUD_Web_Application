# AWS_Flask_CRUD_Web_Application (Continuous Deployment Pipeline)


# Overview
 The goal of this project is to put together everything (test automation,Docker, and GitHub Actions) to setup a Continuous Deployment pipeline.
 
# Requirement covered
  * Setting up a GitHub repository with web service to deploy.
       * This web service is in Flask for this project.
  * Describing the behavior of at least 1 feature in gherkin
  * Write unit tests covering some happy path and failure scenario at minimum.
  * Write a Dockerfile that builds the image for application.
  * Write functional tests to test your feature(s).
  * Configure GitHub actions to do the following:
     * On push to the repo, build the code, run unit tests,and push image to ECR.
     * Deploy the new version to dev environment in ECS
     * Run functional tests against the updated service
     * Deploy the new version to prod in ECS
  * Changes should be seen in dev and prod.


# Quick Start Using Pipenv

```

# Activate venv
$ pipenv shell

# Install dependencies
$ pipenv install

# Create db
 Delete db.sqlite file if you want to create new tables, otherwise it will be automatically created
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

## STEPS To do through CLI:
### Setup your AWS CLI
* Go to [AWS docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and follow the instructions to install the AWS CLI on your operating system. Note: for Windows users in WSL, this will  be Linux.
* Follow the instructions in the [configuration section]https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) of the docs to get setup in AWS.

### Build, tag, and push Docker image to ECR
* Navigate to [ECR](https://us-west-2.console.aws.amazon.com/ecr/repositories?region=us-west-2)
* Click on the ECR repository with your username on it.
* Click on "View Push Commands" button on the top right.
* Change directory in your terminal to the flask docker image you created.
* Follow the instructions from the push commands to log into ECR then build, tag, and push your flask image.
### Redeploy Application
* Go to the Clusters page in ECS and navigate to the cluster with your username on it
* Click on your service
* Click Update on the top-right
* Check the box labeled Force New Deployment.
* Click Skip to Review at the bottom of the page
* Click Update Service
* Click View Service
* Click on the Details tab
* Click on the Target Group's name
* When that target group show's healthy, your service is now reachable
* Click on the Load Balancer
* Copy its DNS name into your browser, and you should see your application landing page.

# UI Screenshot

![Image of UI](https://github.com/nilaynarlawar/AWS_Flask_CRUD_Web_Application/blob/main/UI%20Screenshot.png)

# References
  * https://www.youtube.com/watch?v=PTZiDnuC86g&t=705s
  * https://github.com/bradtraversy/flask_sqlalchemy_rest
  * https://youtu.be/XTpLbBJTOM4
  * https://codeloop.org/flask-crud-application-with-sqlalchemy/
