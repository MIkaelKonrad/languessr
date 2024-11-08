import pandas as pd 
import csv 


class Score_Tracker:
    def __init__(self,lat_guess,lng_guess,score, distance):
        self.lat_guess = lat_guess
        self.lng_guess = lng_guess
        self.score = score
        self.distance = distance

    def save(self):
        with open('Score_tracking.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.lat_guess, self.lng_guess, self.score,self.distance])
            file.close()

    def print(self):
        print(self.lat_guess)
    
    def new(self):
        with open('Score_tracking.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['lat_guess', 'lng_guess', 'score','distance'])
            file.close()



