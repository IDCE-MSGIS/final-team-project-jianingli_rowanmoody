## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python
The purpose of this script is to extract the 5-day weather forecast for a particular latitude and longitude from the National Weather Service website.  The user inputs include the latitude and longitude of a particular location (in this case Worcester, MA), and the outputs include the URL of the desired weather forecast and the 5-day forecast.

The edits made to the original script include the addition of a more effective user input option, the inclusion of the URL output of the input location, and efforts to clean the output forecast in regards to word spacing and uppercase letter use.  Within the body of the script, the input latitude and longitude values are converted to strings to better be concatenated into the output URL, and the replace function was used to both fix the spacing errors and to change text to uppercase strings in the forecast output.  The addition of the user prompt option allows this script to more easily be used for any location without prior user knowledge of Python script.  

One difficulty that was encountered while editing the original script was in identifying which output strings needed cleaning with the replace function.  This debugging process was especially tedious as different lines of the output included similar phrases and different syntax solutions were required.  


## Final Project: Script 2
### Lady Slipper Orchid Suitability
The goal of this script is to create a streamlined method of judging the suitability of a habitat for the species of orchid, the Pink Lady's Slipper (Cypripedium acaule Ait).  The suitability is based on three environmental variables important for the orchid, including the presence of a symbiotic fungus (of the Rhizoctonia genus), light levels, and moisture levels.  As the presence of the fungus is crucial for the orchid to receive the necessary nutrients it needs germinate, this variable acts as a Boolean value in terms of habitat suitability.  This orchid enjoys low and mid-levels of light availability, with high levels being unsuitable for habitation.  Moisture levels are important for this orchid, as it prefers moist conditions, can tolerate mid-level moisture levels, and is unable to grow in low moisture conditions.  These variables make up the input variables for the function ‘Suitability’.  

######  Fungus Presence: y/n 
######  Light Level: high/mid/low
######  Moisture Level: high/mid/low

When this function is run, the user is prompted with three rounds of input opportunities, one for each input variable.  This allows the user to better understand the information necessary for the function, and to be able to utilize it without having prior knowledge of Python programming.  The result of this function is a judgement of the suitability of the environment described by the input variables in three levels; “Habitat suitable”, “Habitat partially suitable”, and “Habitat unsuitable”.  

While the structure of this function was relatively easy to code, it took some time to properly organize the variables within the conditional statements to properly represent their relationship with the orchid species in question.  The first version of this function did not include the option for raw_input, instead relying on the user’s ability to properly organize their input variables into the function directly.  Great thought was put into the effectiveness of each prompt to increase the ability for a user to accurately describe the environment in question within the variable ranges presented within each prompt.  While this function is very specifically organized around the Lady Slipper species, it could be modified to work as a suitability classifier for any species or occurrence.  Future work could be done to increase flexibility in variable ranges, perhaps even including a weighted variable option to take into consideration the importance of each variable in question.  
