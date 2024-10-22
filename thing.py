import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#menu display
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('|CS 021 Final Project|')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('Welcome to the first Version of Oscar Drings Solar Tracking Algorithm!')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('The purpose of this algorith is to help a solar designer optimize the angle of a solar array throughout the day, based on its location, to maximize its output.')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------')
# Define the latitude and the time step (in hours)
LATITUDE = int(input('Please enter a latitude you would like to know the Solar Altitude and Panel Azumith for a region in the Northern Hemisphere between (0-90 degrees):'))

if LATITUDE < 0 or LATITUDE > 90:
  print('Im sorry, input is not within the scope of this Tracking Algorithm.Panel')
  LATITUDE = int(input('Please enter a latitude you would like to know the Solar Altitude and Panel Azumith for a region in the Northern Hemisphere between (0-90 degrees):'))


LATITUDE = LATITUDE + 32 
#LATITUDE = 45
TIME_STEP = 1

# Define the solar declination angle (in degrees) as a function of time (in days)
def solar_declination(time):
  return 23.45 * math.sin(math.radians(360 * (time - 173) / 365))

# Define the hour angle (in degrees) as a function of time (in hours)
def hour_angle(time):
  return 15 * (time - 12)

# Define the solar altitude angle (in degrees) as a function of time (in hours)
def solar_altitude(latitude, time):
  declination = solar_declination(time / 24)
  angle = hour_angle(time)
  return math.degrees(math.asin(math.sin(math.radians(latitude)) * math.sin(math.radians(declination)) + math.cos(math.radians(latitude)) * math.cos(math.radians(declination)) * math.cos(math.radians(angle))))

# Define the solar azimuth angle (in degrees) as a function of time (in hours)
def solar_azimuth(latitude, time):
  declination = solar_declination(time / 24)
  altitude = solar_altitude(latitude, time)
  angle = hour_angle(time)
  return math.degrees(math.acos((math.sin(math.radians(altitude)) * math.sin(math.radians(declination)) - math.sin(math.radians(latitude))) / (math.cos(math.radians(altitude)) * math.cos(math.radians(declination)))))


# Calculate the solar altitude and azimuth angles for each hour
altitudes = []
azimuths = []
for time in range(0, 24, TIME_STEP):
  altitudes.append(solar_altitude(LATITUDE, time))
  azimuths.append(solar_azimuth(LATITUDE, time))

# Plot the solar altitude and azimuth angles
plt.plot(altitudes, label="Altitude")
plt.plot(azimuths, label="Azimuth")
plt.title("Graph")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Degree")
plt.show()

img = mpimg.imread('picture.png')
imgplot = plt.imshow(img)
plt.show()
