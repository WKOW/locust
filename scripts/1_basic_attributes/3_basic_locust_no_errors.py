from locust import User, task, between, constant
from datetime import datetime

class MyWebUser(User):
    #wait_time = between(1, 10)
    wait_time = constant(2);
    #wait_time =  constant_pacing(7)

    @task
    def login_URL(self):
        print("I am loggin into device")
        print(datetime.now())

    @task
    def login_URL2(self):
        print("I am loggin into deviceAaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(datetime.now())
