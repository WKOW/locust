from locust import HttpUser, SequentialTaskSet, task, between


class UserBehaviour(SequentialTaskSet):
    @task
    def go_to_agent_lookup(self):
        resp1 = self.client.get("/InsuranceWebExtJS/agent_lookup.jsf", name="Agent Lookup")
        print(resp1.status_code)
        print(resp1.headers)
        # how to check is response is correct
        assert "Search by Agent Name" in resp1.text

    @task
    def post_all_agents(self):
        resp2 = self.client.post("/InsuranceWebExtJS/agent_lookup.jsf", name="Post All Agents", data={"show-all": "show-all",
                                                                          "show-all:search-all.x": "43",
                                                                          "show-all:search-all.y": "8"})
        print(resp2.status_code)
        print(resp2.headers)
        # how to check if response is correct
        assert "Search by Agent Name" in resp2.text

class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://demo.borland.com"
    tasks = [UserBehaviour]
