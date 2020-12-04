from locust import User, task, between
from datetime import datetime

class MyWebUser(User):
    wait_time = between(1, 2)
    #wait_time = constant(5);
    #wait_time =  constant_pacing(7)

    @task
    def login_URL(self):
        print("I am loggin into device")
        print(datetime.now())
