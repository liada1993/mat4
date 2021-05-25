
file1 = open('dests.txt','r',encoding='utf8')
Lines = file1.readlines()

dests=list()##List of destination
all_data=dict()##Final summary of all cities according to distance, time of arrival and location of the city
farCity=dict()##Sort distant cities

for Line in  Lines: ##Put all the destinations in a list
    dests.append(Line)


import requests
import urllib
import json

# response.status_code

key="&key=AIzaSyDonYJotGIUCcXHY3TzBj_H3ZCkpDzh_I8"

for data1 in dests: ##Removing all relevant data from Google Maps
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
    
    if 'day' in duration:##Arranging cities that can be reached in more than a day
        time=duration.split()
        one_day=24*int(time[0])
        hour=int(time[2])
        duration=one_day+hour
        duration=str(duration) + ' hours'
     
    Lat_Lon = requests.get(Serviceur2+data1+ key) ##Publishing an exact location of the city
    Lat_Lon= Lat_Lon.content.decode('utf-8')
    Lat_Lon = json.loads(Lat_Lon)
    lng = Lat_Lon['results'][0]['geometry']['location']['lng']
    lat = Lat_Lon['results'][0]['geometry']['location']['lat']

    city=data1
    tap = (distance,duration,lng,lat)
    farCity[city]=distance
    all_data[city]=tap
    
farCitys = sorted(farCity)##Sort the three most distant cities
maxfarCitys = farCitys[:3]  

    
    
print(all_data)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    