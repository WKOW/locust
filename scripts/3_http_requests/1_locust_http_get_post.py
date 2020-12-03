from locust import HttpUser, SequentialTaskSet, task, between

class UserBehaviour(SequentialTaskSet):
    @task
    def findAgent(self):
        self.client.get("/agent_lookup.jsf", name="Agent Lookup")

    @task
    def login(self):
        self.client.post("/agent_lookup.jsf", name="login", data={"show-all": "show-all",
                                                           "show-all:search-all.x": "43",
                                                           "show-all:search-all.y": "8"})

class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://demo.borland.com/InsuranceWebExtJS"
    tasks = [UserBehaviour]
