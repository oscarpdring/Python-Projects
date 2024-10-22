import math
import matplotlib.pyplot as plt

# Define the latitude and the time step (in hours)
LATITUDE = 45
TIME_STEP = 1

# Define the solar declination angle (in degrees) as a function of time (in days)
#delta
def solar_declination(time):
  return 23.45 * math.sin(math.radians(360 * (time - 173) / 365))

# Define the hour angle (in degrees) as a function of time (in hours)
def hour_angle(time):
  return 15 * (time - 12)


# Define the solar altitude angle (in degrees) as a function of time (in hours)
#beta
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

# Define the solar panel tilt angle (in degrees) as a function of time (in hours)
def solar_panel_tilt(latitude, time):
  altitude = solar_altitude(latitude, time)
  tilt = solar_panel_tilt(latitude, time)
  return math.degrees(math.atan2(math.sin(math.radians(altitude)), math.cos(math.radians(altitude)) * math.sin(math.radians(azimuth))))

# Define the solar panel azimuth angle (in degrees) as a function of time (in hours)
def solar_panel_azimuth(latitude, time):
  altitude = solar_altitude(latitude, time)
  azimuth = solar_azimuth(latitude, time)
  return math.degrees(math.atan2(math.cos(math.radians(altitude)) * math.sin(math.radians(azimuth)), math.cos(math.radians(altitude)) * math.cos(math.radians(azimuth))))

# Calculate the solar altitude and azimuth angles for each hour
altitudes = []
azimuths = []
tilt = []
for time in range(0, 24, TIME_STEP):
  altitudes.append(solar_altitude(LATITUDE, time))
  azimuths.append(solar_azimuth(LATITUDE, time))
  tilt.append(solar_panel_tilt(LATITUDE, time))

# Plot the solar altitude and azimuth angles
plt.plot(altitudes, label="Altitude")
plt.plot(tilt, label= "Tilt")
plt.plot(azimuths, label="Azimuth")
plt.title("Graph")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Degree")
plt.show()
