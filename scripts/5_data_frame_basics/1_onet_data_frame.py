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
        print('!!!!!!!! Print dataframe')
        print(df)
        print('!!!!!!!! Print sample row')
        sample = df.sample()
        print(sample)
        print('!!!!!!!! Print values')
        print(sample.loc[sample.index, 'endpoint'].values[0])
        print(sample.loc[sample.index, 'name'].values[0])

        self.client.get(sample.loc[sample.index, 'endpoint'].values[0],
                        name=sample.loc[sample.index, 'name'].values[0])
