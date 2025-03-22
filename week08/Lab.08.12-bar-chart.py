# Bar chart
# Thi program creates a pie chart
# By Ignacio Riboldi

import numpy as np 
import matplotlib.pyplot as plt  


countiesList = ['Mayo', 'Galway', 'Wicklow', 'Dublin','Donegal']

counties = np.random.choice( countiesList ,  
                            p=[0.1, 0.3, 0.2, 0.12, 0.28 ],  
                            size=(100) )  

unique, counts = np.unique(counties, return_counts=True) 

# Bar plot 
plt.bar(unique, counts)  
plt.show() 