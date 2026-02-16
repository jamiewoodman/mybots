import numpy
import matplotlib.pyplot as plt
"""
backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

plt.plot(backLegSensorValues, label ='Back Leg', linewidth=3.5)
plt.plot(frontLegSensorValues, label='Front leg')
plt.legend()
plt.show()
"""
BLtargetAngles = numpy.load('data/targetAnglesBL.npy')
FLtargetAngles = numpy.load('data/targetAnglesFL.npy')
plt.plot(BLtargetAngles, label = 'Back Leg', linewidth=3.5)
plt.plot(FLtargetAngles, label='Front leg')
plt.legend()
plt.show()