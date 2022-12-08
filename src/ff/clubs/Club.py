import os 
import pandas as pd
import ff


class Club():

    def __init__(self, club_dict):
        self.name = club_dict['name']
        self.clubelo_name = club_dict['clubelo_name']
        self.elo_data = self.load_elo_data()

    def load_elo_data(self):
        df = pd.read_csv(os.path.join(ff.PROJECT_ROOT,'data','raw',f'{self.name}_elo.csv'))
        df['From'] = pd.to_datetime(df['From'], format="%Y-%m-%d")
        df['To'] = pd.to_datetime(df['To'], format="%Y-%m-%d")

        return df


    def get_elo(self, date):

        filtered_df = self.elo_data[(date >= self.elo_data['From']) & (date < self.elo_data['To'])]

        return filtered_df['Elo'].iloc[0]
