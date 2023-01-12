# random station number: 505307
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/505307'

weather = get(url).json()

#first_record = weather['items'][0]

# Use for loop to iterate over temps and add to a list
#temperatures = []
#for record in weather['data']:
#    temperature = record['ambient_temp']
#    temperatures.append(temperature)

# list comprehension is better
temperatures = [record['ambient_temp'] for record in weather['items']]

# list comprehension for timestamps
#timestamps = [record['reading_timestamp'] for record in weather['items']]

# parse timestamps
timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]

# create plotof timestamps against temp and show it
plt.plot(timestamps, temperatures)

# set axis labels
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.show()
