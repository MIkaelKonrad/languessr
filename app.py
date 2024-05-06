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

@app.route('/', methods = ['POST','GET'])
def game():
    df = pd.read_csv('RecordingsList.csv')
    GameSeed = df.sample(n=2)
    lat = GameSeed['Latitude'].iloc[1]
    lng = GameSeed['Longitude'].iloc[1]
    rec = GameSeed['Recording'].iloc[1]
    rec_arr = rec.split('\\')
    n = len(rec_arr)
    rec_dir='\\static'
    i=6
    while i<=n-1:
        rec_dir =  rec_dir + '\\' + rec_arr[i] 
        i = i+1
    print(rec)
    print(rec_dir)
    print(type(lng))
    print(rec_arr[-1])
    return render_template("HTMLPage3.html",LNG = lng, LAT = lat, RECDIR = rec_dir, RECNAME = rec_arr[n-1])


@app.route('/Result')
def result():
    return render_template("HTMLPage2.html")

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



if __name__ == '__main__':
    app.run(debug=True)

 
