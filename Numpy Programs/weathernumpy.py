# Numpy Weather.

# Week report
import numpy as np
temp=np.array([[22,24,25,23,21],[20,22,24,26,25],[18,20,22,24,26],[19,21,23,25,27],[21,23,25,27,29],[23,25,27,29,31],[25,27,29,31,33]])
print('week temperatures::',temp)

# Slicing, Indexing, Shaping, and Reshaping Operations

# Slice the first row (Monday's temperatures)
monday_temps = temp[0]
print('Monday Temperatures::',monday_temps)

# Index the maximum temperature on Wednesday
wednesday_max_temp = temp[2, 4]
print('Maximum temperature of Wednesday::',wednesday_max_temp)

# Reshape the array to a 1D array
temperature_data_1d = temp.flatten()
print('Reshape the array to a 1D array::',temperature_data_1d)

# Shape the array to a 3D array (days, hours, readings)
temperature_data_3d = temp.reshape(7, 1, 5)
print('Shape the array to a 3D array::',temperature_data_3d)


# Calculating Various Statistics

# Calculate the mean temperature for the week
mean_temp = np.mean(temp)
print('The mean temperature for the week::',mean_temp)

# Calculate the standard deviation of temperatures for the week
std_dev_temp = np.std(temp)
print('The standard deviation of temperatures for the week::',std_dev_temp)

# Calculate the maximum and minimum temperatures for the week
max_temp = np.max(temp)
min_temp = np.min(temp)
print('Maximum temperature for the week::',max_temp,' , Minimum temperature for the week::', min_temp)

# Calculate the median temperature for each day
median_temps = np.median(temp, axis=1)
print('The median temperature for each day::',median_temps)
