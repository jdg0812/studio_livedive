from flask import Flask, request, jsonify
import requests
import envVariable
import sqlite3
import json
import helpers
import ranking_script as rank
from flask_cors import CORS



app = Flask(__name__)
cors = CORS(app)
@app.route('/')
def index(): 
    return "This is the root page, use a route"


#http://127.0.0.1:5000/weather?lat=-16.24133&lon=145.86398
@app.route('/weather')
def weather():
    args = request.args
    latitude = args.get('latitude')
    longitude = args.get('longitude')
    reqURL = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly,daily,alerts&appid={}'.format(latitude, longitude, envVariable.api_key)
    response = requests.get(reqURL).json()
    #current_temperature = response.get('main', {}).get('temp')
    #print(reqURL)
    # print("Latitude is: " + str(response['lat']))
    # print("current weather is: " + str(response['current']))
    # print("current visibility is: " + str(response['current']['visibility']))
    return response


@app.route('/places')
def places():
    
    conn = sqlite3.connect('divebase.db')
    c = conn.cursor()
    query = f"""
        SELECT name
        FROM divesites
        """
    c.execute(query)
    data = c.fetchall()

    conn.close()
    for i in data:
        print(i[0])

    res = json.dumps(data)
    return res

@app.route('/closetPlaces')
def closestPlaces():
    args = request.args
    lat1 = float(args.get('latitude'))
    lon1 = float(args.get('longitude'))

    conn = sqlite3.connect('divebase.db')
    c = conn.cursor()
    query = f"""
        SELECT name, latitude, longitude
        FROM divesites
        """
    c.execute(query)
    data = c.fetchall()
    divespots = []
    distances = []
    latArr = []
    longArr = []
    conn.close()
    #find distance between each recorded point
    for i in data:
        #print("latitude of " + str(i[0]) + " is " + str(i[1]) + " and longitude is " + str(i[2]))
        divespots.append(str(i[0]))
        lat2 = float(i[1])
        lon2 = float(i[2])
        dist = helpers.calculateDistance(lat1, lon1, lat2, lon2)
        distances.append(dist)
        latArr.append(lat2)
        longArr.append(lon2)

    minList = sorted(zip(divespots, distances, latArr, longArr), key=lambda t: t[1])
    retList = list(minList[:5])
    
    calcScore = []
    i = 0
    while i < 5:
        latCalc = float(retList[i][2])
        longCalc = float(retList[i][3])
        #print(latCalc, longCalc)
        c = rank.score_calculator(latCalc,longCalc)
        calcScore.append(c)

        i+=1

    print(calcScore)
    #print(retList)
    j = 0
    resList = []
    for i in retList:
        li = list(i)
        li.append(calcScore[j])
        j+=1
        resList.append(li)

    res = json.dumps(resList)
    #print(res)
    return res


app.run(host='0.0.0.0', port=82)