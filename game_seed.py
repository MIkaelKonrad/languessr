from game_settings import Game_Settings
import pandas as pd
import HandlingRecordingsList as hrl
import csv


class Game_Seed:
    def __init__(self,game_settings):
        self.settings = game_settings
        df = pd.read_csv('RecordingsList.csv')
        df2 = df.Recdf.df_restr(game_settings.country,game_settings.fam,game_settings.lang)
        self.seed = df2.sample(n=5)

    def read(self):
        #with open('seed.csv', 'a', newline='') as file:

        self.settings = self.settings.read()
        df = pd.read_csv('seed.csv')
        self.seed = df 
        print(df)

    def save(self):
        seed_str = self.seed.to_csv('seed.csv')
    
    def choose(self,n):
        self.seed
        lat = self.seed['Latitude'].iloc[n]
        lng = self.seed['Longitude'].iloc[n]

        rec = self.seed['Recording'].iloc[n]
        rec_arr = rec.split('\\')
        m = len(rec_arr)
        rec_dir='\\static'
        i=6
        while i<=m-1:
            rec_dir =  rec_dir + '\\' + rec_arr[i] 
            i = i+1
        return [lng,lat,rec_dir,rec_arr[m-1]]



