import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate 
import matplotlib.ticker as tick

v = plt.figure()
x, y = np.loadtxt('droptower_vdata.txt', float,'#','   ', unpack = True )
print("Time: ", x)
print("Velocity: ", y)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
#set x axis intervals
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(-24, 24,  2.0))
plt.plot(x,y)
plt.savefig('velocity.png')


acceleration = np.diff(y)
a_time = np.delete(x, len(x)-1)
print("Acceleration: ", acceleration)

a=plt.figure()
plt.xlabel('Time (s)')
plt.ylabel('Acceleration ( $m^2$ /s)')
plt.xticks(np.arange(min(a_time), max(a_time), 1.0))
plt.plot(a_time, acceleration)
plt.savefig('acceleration.png')




position = integrate.cumtrapz(y, initial = 0)
print("Position: " , position)

p=plt.figure()
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.plot(x, position)
plt.savefig('position.png')



