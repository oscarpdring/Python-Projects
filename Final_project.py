import math
import matplotlib.pyplot as plt
import numpy as np

# Define the latitude and the time step (in hours)
LATITUDE = 45
TIME_STEP = 1
P = 0.2 #reflectivity/albeto
n = int(input('Please enter the day of the year in number form(n out of 365):'))

#fixed tilt/azimuth for no/single tracking:
sigma = 45
phiC = 0

#solar time
solar_Time = np.arange(0,24,(1/60))
print(len(solar_Time))

# Define the solar declination angle (in degrees) as a function of time (in days)
def solar_declination(time):
  return 23.45 * math.sin(math.radians(360 * (time - 173) / 365))

# Define the hour angle (in degrees) as a function of time (in hours)
def hour_angle(time):
    H = 15*(12-solar_Time)
    
    cnt = [0,0.2]
    for trackingMode in cnt:
        #n = simDays()
        #claculating solar declination angle:
        delta = 23.45 * math.degrees(math.sin(math.radians(360/365*(n-81))))


        #calculate altitude angle:
        beta = math.degrees(math.asin(math.cos(math.radians(LATITUDE))*math.cos(math.radians(delta))*math.cos(math.radians(H))+math.sin(math.radians(delta))))

        #calculate the solar azimuth:
        phiS = math.degrees(math.asin(math.cos(math.radians(delta)))*math.sin(math.radians(H))/math.cos(math.radian(beta)))

        #Using solar position and tracking conditions to calculate IC, total irradiance from the sun collected:
        A = 1160 + 75* math.degrees(math.sin(math.radians(360/365*(n-275))))
        k = 0.174 + 0.035* math.degrees(math.sin(math.radians((360/365*(n-100)))))
        m = 1/math.degrees(math.sin(math.radians(beta)))
        m = (1/(math.degrees(math.sin(math.radians(beta)))+0.50572*(6.07995+beta)^(-1.6365)))
        m = m.real

        #direct beam insolation (normal to suns rays)
        Ib = A*exp(-k*m)
        if beta<=0:
             Ib=0
        #Collector insolatino calculations:
        #horizontal beam and (isotropic) diffuse insolation from the sun:
        C = 0.095 + 0.04*(math.degrees(math.sin(math.radian(360/365*(n-100)))))
        Ibh = Ib*(math.degrees(math.sin(math.radian(beta))))
        Idh = C*Ib
    return 15 * (time - 12),H
                      
    
    
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
