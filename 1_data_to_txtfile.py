#This code takes into entry Arduino with code "sonar_1avr22", and it produces a txt file with max 1000 (line 15) distances measured

import serial #reading data from port
from datetime import datetime #to automatically write the date and time of measure
import matplotlib.pyplot as plt #to plot the graph live

port_serie = serial.Serial(port = "COM3", baudrate = 9600) #reading port
now_name = datetime.now().strftime("%y%m%d_%H-%M-%S") + ".txt"
now = datetime.now().strftime("%d %b %Y %H:%M:%S")

with open(now_name, "w") as file: #creates and opens a new file
    file.write("Mesure prise le " + now + ", mesurée en mm (0 d.p.)")
    file.write('\n')
    i = 0
    while i<1000: #1000 est le nombre maximal de données
        mesure = port_serie.readline()
        distance = ""
        print(str(i) + " : " + str(mesure))
        for char in str(mesure):
            if char.isdigit():
                distance+=char
        file.write(distance)
        file.write('\n') #leaves a line after writing the distance
        i+=1