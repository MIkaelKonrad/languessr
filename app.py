from flask import Flask, request, jsonify, render_template
import subprocess 
import RecordingClass as rec
import os
import shutil
import pandas as pd

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

    # point 1. from above
    df = pd.read_csv('RecordingsList.csv')
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


''' The below code is used build up the database of samples and therefore not directely relevant for functioning of the game. '''
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


@app.route('/RecCheck', methods = ['POST','GET'])
def RecCheck():
    if request.method == 'POST':
        country = request.form["Country"]
        fam = request.form["fam"]
        lang = request.form["lang"]
        print(fam)
        df = pd.read_csv('RecordingsList.csv')
        if country != "":
            df = df.loc[df['Country'] == country]
        
        if fam != "":
            df = df.loc[df['Language Family'] == fam]
        
        if lang != "":
            df = df.loc[df['Language'] == lang ]
        table = '          <table class="table"> <tr> <th>Country</th>  <th>Language Family</th>  <th>Language</th>  <th>Latitude</th> <th>Longitude</th> <th class="wide-column">Recording</th> <th>Show Location</th> </tr>'
        df= df.reset_index()
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
        df = df.to_csv(header=None, index=False).strip('\n').split('\n')
        return render_template('RecCheck.html', Table = df, Table2 = table )
    elif request.method == 'GET':
        
        return render_template('RecCheck.html', Table = '')
    else :
        return render_template('ReckCheck.html', Table = '')

if __name__ == '__main__':
    app.run(debug=True)

 
