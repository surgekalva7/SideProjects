import math
import os

import requests
import json
import folium
import webbrowser

def getDistanceWilling()->int:
    #returns a valid output of the radius in miles
    temp = input("What is the distance in miles that you are willing to travel: ")
    final = 0
    while(not temp.isdigit() and not int(temp)==0):
        temp = input("What is the distance in miles that you are willing to travel, please enter a valid number: ")
    final = int(temp)
    return final



def getLocation()->[str]:
    # Get the ip address/not that accurate since it is coming from a website
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    temp = data['loc'].split(",")
    return temp


def getRadius(miles)->int():
    #converts from miles to meters
    radius = miles*1610
    return radius

def getDistanceBetween(yourLat,yourLon, newLat,newLon)->float:
    x = abs(yourLon - newLon)*60
    y = abs(yourLat-newLat)*60
    distance = math.sqrt(pow(x,2)+pow(y,2))
    print(distance)
    return distance


def getOptions(m,yourLat,yourLon,miles):
    api_key = 'AIzaSyAYT0q5TPXi3fJb1k2hHftaCq9lnwB9KtM'

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    query = "Local Pizza"
    r = requests.get(url + 'query=' + query +
                     '&key=' + api_key)
    x = r.json()
    y = x['results']
    #print(y)
    tooltip = 'Click For more'

    for i in range(len(y)):
        name = y[i]['name']
        print(name)
        lat = float(y[i]['geometry']['location']['lat'])
        #print(lat)
        lon = float(y[i]['geometry']['location']['lng'])
        #print(lon)
        rating = y[i]['rating']
        #print(rating)
        if(getDistanceBetween(yourLat,yourLon,lat,lon)<miles):
            final = '<strong>{}</strong>'.format(name) + '<br><strong>Rating:{}</strong>'.format(rating) \
                    + '<br><strong>Miles:{}</strong>'.format(round(getDistanceBetween(yourLat,yourLon,lat,lon),2))

            folium.Marker(location=[lat, lon], popup=final, tooltip=tooltip,
                          icon=folium.Icon(icon="cutlery", color='red')).add_to(m)


def main():


    #finding the location of the ip address
    temp_Array=getLocation()

    #getting the miles and converting it into meters
    miles = getDistanceWilling()
    radius = getRadius(miles)

    #creating a latitude and a longitude
    lat = temp_Array[0]
    lon = temp_Array[1]

    # creating a map object
    m = folium.Map(location = [float(lat),float(lon)], zoom_start = 12)
    getOptions(m,float(lat),float(lon),miles)

    #Global
    tooltip = 'Click For more'

    #creating a marker
    folium.Marker([lat,lon], popup= '<strong>Your Location</strong>', tooltip=tooltip).add_to(m)

    #circle marker
    folium.Circle(location=[lat,lon], radius=radius,popup = "The current radius",color = '#b00050',fill=True,fill_color = '#b00050').add_to(m)


    #create a html page of the map
    m.save('map.html')
    webbrowser.open('file://' + os.path.realpath('map.html'))





if __name__ == "__main__":
    main()
