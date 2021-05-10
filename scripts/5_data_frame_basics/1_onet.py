from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://wiadomosci.onet.pl"

    @task()
    def get_only_onet(self):
        self.client.get("/tylko-w-onecie", name="Tylko w Onecie")

    @task()
    def get_politico(self):
        self.client.get("/politico", name="Politico")

