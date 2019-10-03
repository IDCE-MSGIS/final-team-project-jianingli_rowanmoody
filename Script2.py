'''
Jianing Li & Rowan Moody
IDCE 302 - Lady Slipper Suitability Project
Time Taken 3:30
'''

#The function 'Suitablity' takes three environmental variables (sympbiotic fungi presence, availablity of sunlight, and moisture level) and describes the suitability of the inputs for habitation of the orchid species Lady Slipper.

#fungi input y/n , sun input high/mid/low, water input high/mid/low
#User prompted for input
fungi,sun,water=raw_input('Input fungi presence (y/n): '), raw_input ('Input sun strength (high/mid/low): '), raw_input ('Input moisture level (high/mid/low: ')

#Suitability function defined by lady slipper environment parameters
def Suitability (fungi,sun,water):
  if fungi=='y' and (sun=='mid'or sun=='low') and water=='high': #high moisture and low to mid level light is best for orchid
    return 'Habitat suitable'
  elif fungi=='y' and (sun=='mid'or sun=='low') and water=='mid': #mid moisture is partially suitable for orchid
    return 'Habitat partially suitable'
  else: #fungus is necessary for orchid, high light and low water levels are unsuitable for orchid
    return 'Habitat unsuitable'

print Suitability (fungi,sun,water)
