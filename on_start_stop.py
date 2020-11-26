from locust import User, task, between, constant, constant_pacing
from datetime import datetime

class MyWebUser(User):

    # inbuilt wait time methods
    wait_time=between(1,2)
    weight = 3
    # wait_time=constant(3)
    # wait_time=constant_pacing(1,2)

    @task
    def login_URL(self):
     print("I am loggin into URL")

class MyMobileUser(User):

    # inbuilt wait time methods
    wait_time=between(1,2)
    weight = 1
    # wait_time=constant(3)
    # wait_time=constant_pacing(1,2)

    @task
    def login_URL(self):
     print("I am loggin into Mobile URL")