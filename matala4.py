
file1 = open('dests.txt','r',encoding='utf8')
Lines = file1.readlines()

dests=list()
all_data=dict()
farCity=dict()

for Line in  Lines:
    dests.append(Line)
# print(dests)

import requests
import urllib
import json

# response.status_code

key="&key=AIzaSyDonYJotGIUCcXHY3TzBj_H3ZCkpDzh_I8"

for data1 in dests:
    Serviceurl ="https://maps.googleapis.com/maps/api/distancematrix/json?"
    Serviceur2="https://maps.googleapis.com/maps/api/geocode/json?address="
    parms = dict()
    parms['origins']='תל אביב'
    parms['destinations'] = data1
    parms['key'] = 'AIzaSyDonYJotGIUCcXHY3TzBj_H3ZCkpDzh_I8' 
    url = Serviceurl + urllib.parse.urlencode(parms)
    response = requests.get(url) 
    data=response.content.decode('utf-8')
    data=json.loads(data)
    distance=data['rows'][0]['elements'][0]['distance']['text']
    duration=data['rows'][0]['elements'][0]['duration']['text']
    
    if 'day' in duration:
        time=duration.split()
        one_day=24*int(time[0])
        hour=int(time[2])
        duration=one_day+hour
        duration=str(duration) + ' hours'
     
    Lat_Lon = requests.get(Serviceur2+data1+ key)
    Lat_Lon= Lat_Lon.content.decode('utf-8')
    Lat_Lon = json.loads(Lat_Lon)
    lng = Lat_Lon['results'][0]['geometry']['location']['lng']
    lat = Lat_Lon['results'][0]['geometry']['location']['lat']

    city=data1
    tap = (distance,duration,lng,lat)
    farCity[city]=distance
    all_data[city]=tap
    
farCitys = sorted(farCity)
maxfarCitys = farCitys[:3]  

    
    
print(maxfarCitys)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    