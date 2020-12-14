from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://allegro.pl"

    @task(1)
    def getHome(self):
        self.client.get("/dzial/dom-i-ogrod", name = "Get Home and Garden")

    @task(5)
    def getAppliances(self):
        self.client.get("/dzial/elektronika", name = "Get Appliances")

    @task(1)
    def getFashion(self):
        self.client.get("/dzial/moda", name = "Get Fashion")
