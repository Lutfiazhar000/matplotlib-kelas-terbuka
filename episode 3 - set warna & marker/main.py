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

t2,y2 = sinusGenerator(1,1,4,90)
plt.plot(t2,y2, 'g')

t3,y3 = sinusGenerator(1,1,4,70)
plt.plot(t3,y3, 'r--')

t4,y4 = sinusGenerator(1,1,4,50)
plt.plot(t4,y4, 'm-o')


# menampilkan plot
plt.show()