# Extra exercise 
# This program show the inflation of a country during the years
# By Ignacio Riboldi

import numpy as np 
import matplotlib.pyplot as plt 

years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
inflation = [-0.9,-1.1,40.9,3.7,6.1,12.3,9.8,8.5,7.2,7.7,10.9,9.5,10.8,10.9,23.9,26.9,40.5,24.8,47.6,53.8,36.1,50.9,94.8,211.4,117.8]

plt.plot(years, inflation)

plt.title("Argentina inflation") 
plt.xlabel("Year") 
plt.ylabel("IPC") 

plt.show()