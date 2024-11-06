from flask import Flask, request, jsonify, render_template
import subprocess 
import RecordingClass as rec
import os
import shutil
import pandas as pd
import numpy as np
import HandlingRecordingsList as hrl

app = Flask(__name__)

@app.route('/Start', methods = ['POST','GET'])
def home():
    return render_template("HTMLPage1.html")

@app.route('/Summary', methods = ['POST','GET'])
def Summary():
    return render_template("Summary.html")


''' What the below function does:
        1. chooses a samples from the list
        2. retrieves latitude and longitude of the sample 
        3. builds a directory of the mp3 file useable in html from the directory contained in the sample 
        4. displays HTMLPage3.html '/'
        5. passes lattitude longitude and the directory of the sample to HTMLPage3 

    Note:   Goal is to change the below code in such a way that five rounds can be played an their scores and locations can be 
            accumulated over these fives rounds. However this requires to change the manner in which variables are passed from 
            HTMLPage3.html to  HTMLPage2.html
'''
@app.route('/', methods = ['POST','GET'])
def game():

    # load current game settings from gameSettings.txt

    game_settings = open('gameSettings.txt','r')
    settings_string = game_settings.read()
    settings_array = settings_string.split(";")
    new_array = []
    for i in settings_array:
        new_array.append(i.split(":"))
    
    country = new_array[0][1]
    fam = new_array[1][1]
    lang = new_array[2][1]

    # point 1. from above
    df = pd.read_csv('RecordingsList.csv')
    df2 = df.Recdf.df_restr(country,fam,lang)
    print(df2)
    GameSeed = df.sample(n=2)

    # point 2. from above
    lat = GameSeed['Latitude'].iloc[1]
    lng = GameSeed['Longitude'].iloc[1]

    # point 3. from above
    rec = GameSeed['Recording'].iloc[1]
    rec_arr = rec.split('\\')
    n = len(rec_arr)
    rec_dir='\\static'
    i=6
    while i<=n-1:
        rec_dir =  rec_dir + '\\' + rec_arr[i] 
        i = i+1
     # Points 4. and 5. from above
    return render_template("HTMLPage3.html",LNG = lng, LAT = lat, RECDIR = rec_dir, RECNAME = rec_arr[n-1])

    
   
     
    


@app.route('/Result')
def result():
    return render_template("HTMLPage2.html")


''' The below code is used to build up the database of samples and therefore not directely relevant for functioning of the game. '''
@app.route('/coordinateCheck', methods = ['POST','GET'])
def coordinate_ceck():
    if request.method == "POST":
        lat = request.form["lat"]
        lng = request.form["lng"]
        country = request.form["Country"]
        fam = request.form["fam"]
        lang = request.form["lang"]
        direc = request.form["rec"]
        src = request.form["src"]
        direcArr = direc.split("\\")
        newDirec = '\\Users\\mikae\\source\\repos\\static\\Recordings\\'+ lang +'\\' + country
        shutil.move(direc,newDirec)
        print(direcArr[-1])
        start = rec.Recording(country,fam,lang,newDirec + '\\' + direcArr[-1],lat,lng,src)
        start.save()
        return render_template("coordinateCheck.html")
    else:
        return render_template("coordinateCheck.html")

@app.route('/doubleCheck', methods = ['POST','GET'])
def double_check():
   
        return render_template('doubleCheck.html')

''' The below code creates a custom html table depending on the users choice of filters. Table will contain info about each 
about each recording fitting the users filter as well as the recording itsself. A button displaying the location of each recording may
be added in the future. 

This Page still has to be linked up with the others.'''
@app.route('/RecCheck', methods = ['POST','GET'])
def RecCheck():
    if request.method == 'POST':
        # the below variables are the filter conditions set by the user.
        country = request.form["Country"]
        fam = request.form["fam"]
        lang = request.form["lang"]
        # below we import the List of the recordings as a pandas dataframe.
        df = pd.read_csv('RecordingsList.csv')
        # we now delete all the rows containing recordings not fitting the users filter
        if country != "":
            df = df.loc[df['Country'] == country]
        
        if fam != "":
            df = df.loc[df['Language Family'] == fam]
        
        if lang != "":
            df = df.loc[df['Language'] == lang ]
        df= df.reset_index()
        # below we generate the html code for the table as a string
        table = '<table class= table> <tr> <th>Country</th>  <th>Language Family</th>  <th>Language</th>  <th>Longitude</th> <th>Latitude</th> <th class="wide-column">Recording</th> <th>Show Location</th> </tr>'
        for index, row in df.iterrows():
            next_row = "<tr> <td>"+row['Country'] +"</td> <td>"+row['Language Family'] +"</td> <td>"+ row['Language'] +"</td> <td>" +str(row['Longitude']) +"</td> <td>" + str(row['Latitude']) +"</td>"
            rec = row['Recording']
            rec_arr = rec.split('\\')
            n = len(rec_arr)
            rec_dir='/static'
            i=6
            while i<=n-1:
                rec_dir =  rec_dir + '/' + rec_arr[i] 
                i = i+1
            recording = '<td> <audio controls> <source src='+rec_dir+' type="audio/mpeg"> Your browser does not support the audio element.</audio> </td>'
            table = table + next_row + recording + ' <td> <Button>Location</Button></td></tr>'
        table = table + " </table>"
        #We now render the page and export the table as Table
        return render_template('RecCheck.html', Table = table )
    elif request.method == 'GET':
        
        return render_template('RecCheck.html', Table = '')
    else :
        return render_template('ReckCheck.html', Table = '')


@app.route('/GameSettings', methods = ['POST','GET'])
def GameSettings():
    if request.method == 'POST':
        country = request.form["Country"]
        fam = request.form["fam"]
        lang = request.form["lang"]
        settings_string = "Country:" + country + "; Language Family:" + fam + "; Language:" + lang + ";"
        game_settings = open('gameSettings.txt','w')
        game_settings.write(settings_string)
        game_settings.close()

    return render_template('GameSettings.html')


if __name__ == '__main__':
    app.run(debug=True)

 
