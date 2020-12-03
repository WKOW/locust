from locust import HttpUser, SequentialTaskSet, task, between


class UserBehaviour(SequentialTaskSet):
    @task
    def findAgent(self):
        resp1 = self.client.get("/agent_lookup.jsf", name="Agent Lookup")
        print(resp1.status_code)
        print(resp1.headers)
        # how to check is response is correct
        if ("Search by Agent Name") in resp1.text:
            resp1.success()
        else:
            resp1.failure("failed to launch url")

    @task
    def login(self):
        resp2 = self.client.post("/agent_lookup.jsf", name="login", data={"show-all": "show-all",
                                                                          "show-all:search-all.x": "43",
                                                                          "show-all:search-all.y": "8"})
        print(resp2.status_code)
        print(resp2.headers)
        # how to check is response is correct
        if ("Here is the list of all available Agents") in resp1.text:
            resp1.success()
        else:
            resp1.failure("failed to launch url")


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://demo.borland.com/InsuranceWebExtJS"
    tasks = [UserBehaviour]
