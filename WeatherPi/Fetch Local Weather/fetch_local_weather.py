from requests import get
import json
from pprint import pprint
from haversine import haversine

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/2696567'

# Lat Long for Geneva House
my_lat = 42.84389687103008
my_lon = -77.01197174537656

all_stations = get(stations).json()['items']

def find_closest():
    smallest = 20036 #longest possible distance(km) between 2 points on Earth
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station

closest_stn = find_closest()

weather = weather + str(closest_stn)

my_weather = get(weather).json()['items']
pprint(my_weather)
        
