import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
for k in range(5):
    for j in range(5):
        length = 1
        width = 1
        height = 1
        x = k
        y = j
        z = .5
        for i in range(10):
            pyrosim.Send_Cube(name="Box"+str(i), pos=[x,y,z] , size=[length,width,height])
            length = length * .9
            width = width * .9
            height = height * .9
            z += (height / 2) + (height / 2 / .9)
pyrosim.End()
