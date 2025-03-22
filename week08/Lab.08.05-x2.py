# X2
# This program choose a random number and multiple itself to get the square.
# By Ignacio Riboldi

import matplotlib.pyplot as plt 
import numpy as np 

xpoints = np.array(range(1,101)) 

ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints) 

plt.show() 