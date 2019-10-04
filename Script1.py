'''
#Jianing Li & Rowan Moody
#Time Taken 1:30
# Assignment title: Final Project- Web-scraping Weather Forecast
# Date: 09/23/2019
# Description: The script web-scrapes the weather.gov website to extract the 5-Day weather forecast for a given location
# Inputs: Latitude & Longitude in Decimal Degrees
# Outputs: 5-Day Weather Forecast
'''

# import required libraries
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []

## Provide the latitude and longitude for the location you would like to check the forecast for
## Lat/lon in decimal degrees provided for Worcester, MA
print ('Please input latitude')
lat = input()
lat = str(lat)
# lat = '42.2634'
print ('please input longitude')
lon = input()
lon = str(lon)
# lon = '-71.8022'
print('Location input complete ! ')

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
# print url
print 'The url is :',url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)

# Print list to remove unicode characters
for day in forecast:
    day = day.replace('Becoming','Becoming ')
    day = day.replace('Frost','Frost ')
    day = day.replace('SunnyThen','Sunny Then')
    day = day.replace('SlightChance','Slight Chance')   
    day = day.replace('Showers','Showers ')
    day = day.replace('Likely','Likely ')
    day = day.replace('Night', ' Night')
    day = day.replace('Chance', 'Chance ')
    day = day.replace('High', ' High')
    day = day.replace('Low', ' Low ')
    day = day.replace('This', 'This ')
    day = day.replace('then', 'then ')
    day = day.upper()
    print day
