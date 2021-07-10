import pandas as pd
import matplotlib.pyplot as plt

fitness_DF = pd.read_csv('evolution_info.csv')
max_arr = fitness_DF['max']
avg_arr = fitness_DF['avg']
min_arr = fitness_DF['min']

plt.plot(max_arr, color='g', label='max fitness')
plt.plot(avg_arr, color='r', label='avg fitness')
plt.plot(min_arr, color='b', label='min fitness')

plt.xlabel('generations')
plt.ylabel('fitness')
plt.legend(loc=0)
plt.show()