# Extra exercise
# Messing with random data
# By Ignacio Riboldi

import matplotlib.pyplot as plt
import numpy as np


countries = ['Argentina', 'Brasil', 'Chile', 'México', 'Colombia', 'Perú', 'Uruguay', 'Paraguay', 'Bolivia', 'Ecuador']

minSalaries = np.random.randint(200, 1000, size=len(countries))
maxSalaries = minSalaries + np.random.randint(500, 1500, size=len(countries))


plt.figure(figsize=(10, 6))
plt.bar(countries, maxSalaries, label='Maximum Salary')
plt.bar(countries, minSalaries, label='Minimum Salary')

plt.xlabel('Countries')
plt.ylabel('Salary')
plt.title('Salaries per Country (south America)')
plt.legend()

plt.tight_layout()
plt.show()