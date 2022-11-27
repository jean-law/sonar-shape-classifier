#takes into input a txt file "name" and returns a png image of the same name with the silhouette of the object

import time
import matplotlib.pyplot as plt
import numpy as np

name = "220422_14-32-07_f8_1"
file_name = name + ".txt"

y=[]
with open(file_name, "r") as file:
    data_lines = file.readlines()[1:]
    for line in data_lines:
        distance = ""
        for char in line:
            if char.isdigit():
                distance+=char
        y.append(int(distance))
        print(y)
fig = plt.figure()
plt.plot(y, color='black')
x = [i for i in range(len(y))]
plt.fill_between(x, y, 300, color='black')
plot_name = name + ".png"
fig.savefig(plot_name)
