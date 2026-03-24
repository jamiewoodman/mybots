import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(5000)

    def Get_Value(self, t):
        try:
            self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        except TypeError:
            self.values[t] = -1.0

    def Save_Values(self):
        numpy.save('data/' + self.linkName + '_sensorValues.npy', self.values)
