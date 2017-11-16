#Sample python script using Restful API with Open Weather API to get temperatures for a city
#pass city name in api then display min and max values
#Script for interview process

import os
import webbrowser

import json
import urllib2
import requests

from StdSuites import seconds
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#req = webdriver.Firefox()
#Sample python script using Restful API with Open Weather API to get temperatures for a city
#pass city name in api then display min and max values

#api.openweathermap.org/data/2.5/weather?q={city name}

#Set up API Key
#Got key from Open Weather Sign Up process
#Key=642cdd4cce669bf88e052abeb3e55f95

#Get the city name from the user input
#Pass the city name in the open API
#print out the final results of min and max temps

cityname = raw_input('Enter city name to get min and max temperatures: ')
print (cityname)

url = 'http://api.openweathermap.org/data/2.5/weather'
#The following works as a call to the get () and hardcoding the request
#response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=642cdd4cce669bf88e052abeb3e55f95')


payload = {'APPID' :'642cdd4cce669bf88e052abeb3e55f95', 'q': cityname}

# Get request using open api, passing in APPID and city name as parameters
# Parse out min and max temps from response object
# if status code is not valid, print message and invalid status code

response = requests.get(url,params = payload)

status = response.status_code

if (response.status_code == 200):

    #print response.status_code
    #print response.headers
    #print response.json()
    #print response.text

    j = response.json()

    print ('Got temps for the City of:'),(cityname)
    print ('Min Temp:'),j['main']['temp_min']
    print ('Max Temp:'),j['main']['temp_max']


else:

    print ('Did not get a valid response code, got'),(status)




