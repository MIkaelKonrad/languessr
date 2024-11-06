
class Game_Settings:
    def __init__(self,country,fam,lang):
        self.country = country
        self.fam = fam
        self.lang = lang
        
    def save(self):
        settings_string = "Country:" + self.country + "; Language Family:" + self.fam + "; Language:" + self.lang + ";"
        game_settings = open('gameSettings.txt','w')
        game_settings.write(settings_string)
        game_settings.close()

    def read(self):
        game_settings = open('gameSettings.txt','r')
        settings_string = game_settings.read()
        settings_array = settings_string.split(";")
        new_array = []
        for i in settings_array:
            new_array.append(i.split(":"))
    
        self.country = new_array[0][1]
        self.fam = new_array[1][1]
        self.lang = new_array[2][1]
    
    def print(self):
        print('Country: ' + self.country)
        print('Language Family: ' + self.fam)
        print('Language: ' + self.lang)
