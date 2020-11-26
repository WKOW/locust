from locust import HttpUser, task, between, constant, constant_pacing
from datetime import datetime

class MyUser(HttpUser):

    # inbuilt wait time methods
    wait_time=between(1,3)
    # wait_time=constant(3)
    # wait_time=constant_pacing(1,2)
    host="http://newtours.demoaut.com/"

    @task
    def login_URL(self):
     print(datetime.now())