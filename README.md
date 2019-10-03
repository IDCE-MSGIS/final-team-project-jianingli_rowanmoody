## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python
In this lab, you will work with a script that scrapes the 5-day weather forecast from the National Weather Service website. The script extracts information from multiple elements listed under the same class name using the BeautifulSoup library. 

- Copy the **NWS_WeatherForecast.py** file and paste it into the online Python compiler: https://repl.it/languages/python
Make sure you are using Python version 2.7. You can check the Python version in the compiler window on the right.

- Read the description and comments in the script to understand the purpose of the script

- Run the script. You will see some packages being installed in the compiler window when you run it for the first time.

- The script returns the 5-day forecast for Worcester, MA (Lat: 42.2634, Lon: -71.8022) with the latitude and longitude information provided. Using the latitude and longitude values, it generates the following URL through string concatenation: https://forecast.weather.gov/MapClick.php?lat=42.2634&lon=-71.8022

- Open this URL in a Firefox or Chrome browser. Locate the information that is being outputted in our script. Right click on this and select the Inspect Element option. This will launch the Inspector window that helps locate different elements on the page.

- Notice that all forecast containers in this section are located in the _forecast-tombstone_ class inside the _li_ tag. In order to scrape multiple elements listed under the same class name, we utilize the _findAll()_ function from BeautifulSoup. The tag and class names are required arguments for this function.

### Edit the NWS_ WeatherForecast.py script to add the following functionality:
1. Take latitude and longitude values as inputs in decimal degrees from user

2.	Convert the latitude and longitude values to strings to generate the URL for the selected location. Pass this URL as an argument in the _get()_ request.

3.	The returned forecast information did not preserve its spacing during the scraping process. Using the _replace()_ function, fix any spacing issues with the output

4.	Convert the final output to uppercase

Remember to update the Script1.py file to include comments and documentation in your script to tell me what it’s doing!

## Final Project: Script 2
### Lady Slipper Orchid Suitability
The goal of this script is to create a streamlined method of judging the suitability of a habitat for the species of orchid, the Pink Lady's Slipper (Cypripedium acaule Ait).  The suitability is based on three environmental variables important for the orchid, including the presence of a symbiotic fungus (of the Rhizoctonia genus), light levels, and moisture levels.  As the presence of the fungus is crucial for the orchid to receive the necessary nutrients it needs germinate, this variable acts as a Boolean value in terms of habitat suitability.  This orchid enjoys low and mid-levels of light availability, with high levels being unsuitable for habitation.  Moisture levels are important for this orchid, as it prefers moist conditions, can tolerate mid-level moisture levels, and is unable to grow in low moisture conditions.  These variables make up the input variables for the function ‘Suitability’.  

###  Fungus Presence: y/n
###  Light Level: high/mid/low
###  Moisture Level: high/mid/low

When this function is run, the user is prompted with three rounds of input opportunities, one for each input variable.  This allows the user to better understand the information necessary for the function, and to be able to utilize it without having prior knowledge of Python programming.  The result of this function is a judgement of the suitability of the environment described by the input variables in three levels; “Habitat suitable”, “Habitat partially suitable”, and “Habitat unsuitable”.  

While the structure of this function was relatively easy to code, it took some time to properly organize the variables within the conditional statements to properly represent their relationship with the orchid species in question.  The first version of this function did not include the option for raw_input, instead relying on the user’s ability to properly organize their input variables into the function directly.  Great thought was put into the effectiveness of each prompt to increase the ability for a user to accurately describe the environment in question within the variable ranges presented within each prompt.  While this function is very specifically organized around the Lady Slipper species, it could be modified to work as a suitability classifier for any species or occurrence.  Future work could be done to addmore flexibility in variable ranges, perhaps even including a weighted variable option to take into consideration the importance of each variable in question.  


## Final Project: Documentation
### Changing this README
Your write-up will be here, on this README page. You will need to edit this page with your new text: you do **not** need to keep these instructions on your README! 
