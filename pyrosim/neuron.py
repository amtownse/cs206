import math

import pybullet

import pyrosim.pyrosim as pyrosim

import pyrosim.constants as c

class NEURON: 

    def __init__(self,line,bodyid):

        self.Determine_Name(line)

        self.Determine_Type(line)

        self.Search_For_Link_Name(line)

        self.Search_For_Joint_Name(line)

        self.Set_Values(line)

        self.bodyid = bodyid

    def Add_To_Value( self, value ):

        self.Set_Value( self.Get_Value() + value )

    def Get_Joint_Name(self):

        return self.jointName

    def Get_Link_Name(self):

        return self.linkName

    def Get_Name(self):

        return self.name

    def Get_Value(self):

        return self.value

    def Is_Sensor_Neuron(self):

        return self.type == c.SENSOR_NEURON

    def Is_Hidden_Neuron(self):

        return self.type == c.HIDDEN_NEURON

    def Is_Motor_Neuron(self):

        return self.type == c.MOTOR_NEURON

    def Print(self):

        # self.Print_Name()

        # self.Print_Type()

        self.Print_Value()

        # print("")

    def Set_Value(self,value):

        self.value = value

    def Set_Values(self,line):
        
        line = line.split('"')
        self.T = float(line[6])
        self.value = float(line[7])
        self.G = float(line[8])
        self.Z = float(line[9])
        self.I = line[10]
        self.x = 0.0
        if self.Is_Sensor_Neuron() and self.Get_Link_Name()=="zzzzz1":
            self.cpg = [0]*(int(self.T)+1)
            self.cpg[0] = 1

    def Update_Sensor_Neuron(self):

        if self.Get_Link_Name()[0:5]!="zzzzz":

            self.Set_Value(pyrosim.Get_Touch_Sensor_Value_For_Link(self.Get_Link_Name()))

        elif self.Get_Link_Name()[-1]=="1":

            self.Set_Value(self.cpg[0])

            self.cpg.append(self.cpg[0])

            del(self.cpg[0])

        elif self.Get_Link_Name()[-1]=="2":

            self.Set_Value(pybullet.getBasePositionAndOrientation(self.bodyid)[1][0])
        
        elif self.Get_Link_Name()[-1]=="3":
    
            self.Set_Value(pybullet.getBasePositionAndOrientation(self.bodyid)[1][1])

        else:

            self.Set_Value(1)

    def Update_Hidden_Or_Motor_Neuron(self, neurons, synapses):

        self.x=0.0

        for synapse in synapses:

            if synapse[1] == self.Get_Name():

                self.Allow_Presynaptic_Neuron_To_Influence_Me(neurons[synapse[0]], synapses[synapse].Get_Weight())

        #self.x = self.Threshold(self.x)

        self.x-=self.value

        self.x *= self.Threshold(self.T)/2+.5

    def Allow_Presynaptic_Neuron_To_Influence_Me(self, neuron, weight):
 
        self.x+=weight*self.Threshold(neuron.G*(neuron.value+neuron.Z))

    def Update_Hidden_Or_Motor_Neuron_Part2(self):

        self.value = self.value + self.x


# -------------------------- Private methods -------------------------

    def Determine_Name(self,line):

        if "name" in line:

            splitLine = line.split('"')

            self.name = splitLine[1]

    def Determine_Type(self,line):

        if "sensor" in line:

            self.type = c.SENSOR_NEURON

        elif "motor" in line:

            self.type = c.MOTOR_NEURON

        else:

            self.type = c.HIDDEN_NEURON

    def Print_Name(self):

       print(self.name)

    def Print_Type(self):

       print(self.type)

    def Print_Value(self):

       print(self.value , " " , end="" )

    def Search_For_Joint_Name(self,line):

        if "jointName" in line:

            splitLine = line.split('"')

            self.jointName = splitLine[5]

    def Search_For_Link_Name(self,line):

        if "linkName" in line:

            splitLine = line.split('"')

            self.linkName = splitLine[5]

    def Threshold(self):

        self.value = math.tanh(self.value)

    def Threshold(self, value):

        return math.tanh(value)
