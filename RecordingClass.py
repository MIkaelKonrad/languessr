import csv

class Recording:
    def __init__(self,country,family,language,recording,latitude,longitude,source):
        self.Country=country
        self.Family = family
        self.Language=language
        self.Recording=recording
        self.Latitude=latitude
        self.Longitude=longitude
        self.Source = source
    def save(self):
        with open('RecordingsList.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.Country, self.Family, self.Language,self.Recording,self.Latitude,self.Longitude,self.Source])
            file.close()
