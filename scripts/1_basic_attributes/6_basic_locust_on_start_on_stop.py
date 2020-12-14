from locust import User,task,between

class MyUser(User):

    wait_time=between(1,2)

    def on_start(self):
     print("I am loggin in")

    @task
    def login_URL(self):
     print("I am doing my work")\

    @task
    def login2_URL(self):
     print("I am doing my another work")

    def on_stop(self):
     print("I am loggin out")