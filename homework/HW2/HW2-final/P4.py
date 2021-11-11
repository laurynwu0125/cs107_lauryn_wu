import numpy as np
import matplotlib.pyplot as plt
import datetime
import math

### Closure defined up here
def clock(r):

    # Inner function to return the x, y coordinate of the clock hand
    def hand_angle(theta):
        nonlocal r
        thetaRad = theta * math.pi / 180
        x = r * math.cos(thetaRad)
        y = r * math.sin(thetaRad)
        return x, y

    return hand_angle

# Get current time
currentDT = datetime.datetime.now()
hour = currentDT.hour
minute = currentDT.minute
second = currentDT.second

# Calculate theta in degrees for each hand
theta_hour = 90 - 30 * hour - minute / 2
theta_minute = 90 - 6 * minute
theta_second = 90 - 6 * second

# Specify the length of hour, minute and second hands
r_hour = 6
r_minute = 8
r_second = 10

# hour_hand = name_of_closure(length_of_hour_hand)
hour_hand = clock(r_hour)
minute_hand = clock(r_minute)
second_hand = clock(r_second)

# x_hour, y_hour = hour_hand(theta_hour)
x_hour, y_hour = hour_hand(theta_hour)
x_minute, y_minute = minute_hand(theta_minute)
x_second, y_second = second_hand(theta_second)

# Plot the clock
plt.plot([0, x_hour], [0, y_hour], linewidth=5)
plt.plot([0, x_minute], [0, y_minute], linewidth=3)
plt.plot([0, x_second], [0, y_second], linewidth=1)
plt.xlim([-r_second, r_second])
plt.ylim([-r_second, r_second])
plt.show()
