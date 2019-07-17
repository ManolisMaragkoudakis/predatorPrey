import numpy as np 
import matplotlib.pyplot as plt 
import predatorPreyLib as ppl

x0 = 1.0
y0 = 1.0
a = 2./3.
b = 4./3.
c = 1.
d = 1.

dt = 1e-4
totalTime = 50.

myArray = np.array([x0,y0,a,b,c,d,dt])
system1 = ppl.ecoSystem(myArray, totalTime)
time = system1.giveTime()
prey = system1.givePrey()
pred = system1.givePred()

plt.figure(1)
plt.plot(time, prey, label = 'prey', color='red')
plt.plot(time, pred, label = 'predator', color='black')
plt.legend(loc='best')
plt.xlabel(r'time ($\rm s$)')
plt.ylabel(r'Population ($\rm AU$)')
plt.title(r'Time evolution of populations.')

myArray2 = np.array([1.5*x0,1.5*y0,a,b,c,d,dt])
system2 = ppl.ecoSystem(myArray2, totalTime)
prey2 = system2.givePrey()
pred2 = system2.givePred()

myArray3 = np.array([2.*x0,2.*y0,a,b,c,d,dt])
system3 = ppl.ecoSystem(myArray3, totalTime)
prey3 = system3.givePrey()
pred3 = system3.givePred()

plt.figure(2)
plt.plot(prey, pred, label='pequeño')
plt.plot(prey2, pred2, label = 'mediano')
plt.plot(prey3, pred3, label = 'grande')
plt.legend(loc='best')
plt.xlabel(r'population of preys ($\rm AU$)', color='red')
plt.ylabel(r'population of predators ($\rm AU$)', color='grey')
plt.title(r'Phase space')
plt.show()
