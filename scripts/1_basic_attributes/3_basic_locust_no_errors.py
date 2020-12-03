from locust import User, task, between


class MyWebUser(User):
    wait_time = between(1, 2)

    @task
    def login_URL(self):
        print("I am loggin into Web device")
        print(datetime.now())


class MyMobileUser(User):
    wait_time = between(1, 2)

    @task
    def login_URL(self):
        print("I am loggin into Mobile device")
        print(datetime.now())
