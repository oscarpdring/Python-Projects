"""
Oscar Dring
CS021 Final Project
12/8/2022
"""


#math libary for trigonometry
import math
#pyplot for ploting the results of the algorithm
import matplotlib.pyplot as plt
#.image for "ploting" the image from the files
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


# Define the latitude and the time step (in hours)
#LATITUDE = 1
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

# Define the solar panel tilt angle (in degrees) as a function of time (in hours)
def solar_panel_tilt(latitude, time):
  altitude = solar_altitude(latitude, time)
  return 90 - altitude

# Calculate the solar altitude and panel tilt angles for each hour
altitudes = []
tilt_angles = []
#for a full day
for hour in range(24):
  altitudes.append(solar_altitude(LATITUDE, hour))
  tilt_angles.append(solar_panel_tilt(LATITUDE, hour))

# Plot the solar altitude and panel tilt angles

plt.subplot(1,2,1)#row 1, col 2, index 1
plt.plot(altitudes, label='Solar Altitude')
plt.plot(tilt_angles, label='Solar Panel Tilt')
plt.xlabel('Time (hours)')
plt.ylabel('Angle (degrees)')
plt.title('Graph of Solar Altitude and Solar Panel Tilt')
plt.legend()


plt.subplot(1,2,2)#row 1, col 2, index 1
img = mpimg.imread('picture.png')
imgplot = plt.imshow(img)
plt.show()


