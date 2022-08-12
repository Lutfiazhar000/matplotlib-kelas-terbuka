import numpy as np
import matplotlib.pyplot as plt

# membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t,y

# membuat plot
t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,90)
t3,y3 = sinusGenerator(1,1,4,180)
t4,y4 = sinusGenerator(1,1,4,50)

dataPlot1 = plt.plot(t1,y1)
dataPlot2 = plt.plot(t2,y2)
dataPlot3 = plt.plot(t3,y3)
dataPlot4 = plt.plot(t4,y4)

# setting properties
plt.setp(dataPlot1,color='r', linestyle='-.', linewidth = 4)
plt.setp(dataPlot2,color='y', linestyle='solid', linewidth = 1)
plt.setp(dataPlot3,color='b', linestyle=':', linewidth = 2)
plt.setp(dataPlot4,color='g', linestyle='dashed', linewidth = .5)

# menampilkan plot
plt.show()


