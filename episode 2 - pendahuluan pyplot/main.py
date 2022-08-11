import numpy as np
import matplotlib.pyplot as plt

'''
1. membuat data
2. membuat plot
3. menampilkan plot

'''

# membuat data 
x = np.array([1,2,3,4,5,6])
y = np.array([1,4,9,16,25,36])
y2 = np.array([1,16,81,256,625,1296])

# membuat plot
plt.plot(x,y)
plt.plot(x,y2)

# menampilkan plot
plt.show()