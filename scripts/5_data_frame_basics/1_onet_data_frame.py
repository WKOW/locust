from locust import HttpUser, task, between
import pandas as pd


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://wiadomosci.onet.pl"

    def __init__(self, parent):
        super().__init__(parent)
        self.df = pd.read_excel('data.xlsx', sheet_name='onet')

    @task()
    def get(self):
        # take data randomly
        df = self.df
        print(df)
        print('!!!!!!!!')
        df = df.sample()
        print(df)
        print('!!!!!!!!')
        print('!!!!!!!!')
        print(df.loc[df.index, 'endpoint'].values[0])
        print(df.loc[df.index, 'name'].values[0])

        self.client.get(df.loc[df.index, 'endpoint'].values[0],
                        name=df.loc[df.index, 'name'].values[0])
