from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'

weather = get(url).json()

weather2 = get(weather['next']['$ref']).json()
