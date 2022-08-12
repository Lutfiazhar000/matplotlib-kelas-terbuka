import numpy as np
import matplotlib.pyplot as plt

# membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t,y

# membuat plot
t1,y1 = sinusGenerator(1,1,4,0)
plt.plot(t1,y1)

# set axis
plt.axis([0,4,-2,2]) # plt.axis(xmin,xmax,ymin,ymax)

# menampilkan plot
plt.show()


