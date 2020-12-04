from locust import User, TaskSet, between, events, task


class MyUser(User):
    wait_time = between(1, 2)

    def on_start(self):
        print("I am loggin in")

    @task()
    class UserBehaviour(TaskSet):

        @task(4)
        def doing_work(self):
            print("I work from monday to thursday")

        @task(1)
        def doing_work_friday(self):
            print("I work on friday")

    def on_stop(self):
        print("I am loggin out")
