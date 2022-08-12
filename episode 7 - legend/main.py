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

# tipe 1
# plt.plot(t1,y1, label="sin(0)")
# plt.plot(t2,y2, label="sin(90)")
# plt.legend

# # tipe 2
# plt.plot(t1,y1, label="sin(0)")
# plt.plot(t2,y2, label="sin(90)")
# plt.legend(loc='upper center')

# # tipe 3
# plt.plot(t1,y1, label="sin(0)")
# plt.plot(t2,y2, label="sin(90)")
# plt.legend(loc='upper center', bbox_to_anchor=(1,2,1))

# tipe 4
plt.figure(1)
ax = plt.subplot(111)
plt.plot(t1,y1, label="sin(0)")
plt.plot(t2,y2, label="sin(90)")
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.7, box.height])
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))


# menampilkan plot
plt.show()