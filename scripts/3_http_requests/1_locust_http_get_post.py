from locust import HttpUser, SequentialTaskSet, task, between

class UserBehaviour(SequentialTaskSet):
    @task
    def go_to_agent_lookup(self):
        self.client.get("/InsuranceWebExtJS/agent_lookup.jsf", name="Agent Lookup")

    @task
    def post_all_agents(self):
        self.client.post("/InsuranceWebExtJS/agent_lookup.jsf", name="Post All Agents", data={"show-all": "show-all",
                                                           "show-all:search-all.x": "43",
                                                           "show-all:search-all.y": "8"})

class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://demo.borland.com"
    tasks = [UserBehaviour]
