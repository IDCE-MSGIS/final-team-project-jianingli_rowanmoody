'''
Jianing Li & Rowan Moody
IDCE 302 - Lady Slipper Suitability Project
Time Taken 3:00
'''

#The function 'Suitablity' takes two environmental variables (sympbiotic fungi presence, availablity of sunlight) and describes the suitability of the inputs for habitation of the orchid species Lady Slipper.

#fungi input y/n , sun input high/mid/low
#User prompted for input
fungi,sun=raw_input('Input fungi presence (y/n): '), raw_input ('Input sun strength (high/mid/low): ')

#Suitability function defined by lady slipper environment parameters
def Suitability (fungi,sun):
  if fungi=='y' and sun=='mid': #mid level light is best for orchid
    return 'Habitat suitable'
  elif fungi=='y' and sun=='low': #low level light is partially suitable for orchid
    return 'Habitat partially suitable'
  else: #fungus is necessary for orchid, high light levels are unsuitable for orchid
    return 'Habitat unsuitable' 

print Suitability (fungi, sun)
