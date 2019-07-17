import numpy as np 

class ecoSystem:

    def __init__(self, myArray=np.zeros(7), timeOfSimulation=0.):

        self.initPrey = myArray[0]
        self.initPred = myArray[1]
        self.a = myArray[2] # constant for growth of preys 
        self.b = myArray[3] # constant for death of preys
        self.c = myArray[4] # constant for growth of preds
        self.d = myArray[5] # constant for death of preds

        self.dt = myArray[6]
        self.totalTime = timeOfSimulation
        self.time = np.arange(0.,self.totalTime,self.dt)

        self.arrayLength = int(len(self.time))
        self.populationPrey = np.zeros(self.arrayLength)
        self.populationPred = np.zeros(self.arrayLength)

        self.populationPrey[0] = self.initPrey
        self.populationPred[0] = self.initPred

    def computePrey(self, previousPrey, previousPred):
        return previousPrey + self.dt * (self.a*previousPrey - self.b*previousPred*previousPrey)

    def computePred(self, previousPrey, previousPred):
        return previousPred + self.dt * (self.d*previousPrey*previousPred - self.c*previousPred)

    def givePrey(self):

        for i in np.arange(1.,self.arrayLength):
            idxTime = int(i)
            self.populationPrey[idxTime] = self.computePrey(self.populationPrey[idxTime-1], self.populationPred[idxTime-1])
            self.populationPred[idxTime] = self.computePred(self.populationPrey[idxTime-1], self.populationPred[idxTime-1])

        return self.populationPrey

    def givePred(self):

        for i in np.arange(1.,self.arrayLength):
            idxTime = int(i)
            self.populationPrey[idxTime] = self.computePrey(self.populationPrey[idxTime-1], self.populationPred[idxTime-1])
            self.populationPred[idxTime] = self.computePred(self.populationPrey[idxTime-1], self.populationPred[idxTime-1])

        return self.populationPred

    def giveTime(self):
        return self.time