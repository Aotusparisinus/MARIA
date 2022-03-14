
import serial
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
 
 
i = 0
column_names = ["Humidity (%)", "Temperature (C)", "Limunosity (lx)", 'Noise (dB)']
# lets make an empty dataframe with the labels for each of the entries that will be received from the microcontroller, a generic Arduino Nano.
# empty = "Temperature (C)": [], "Humidity (%)":["0"], "Limunosity (lx)":["0"], 'Noise (dB)':["0"]}
df = pd.DataFrame(columns = column_names)
ser = serial.Serial("/dev/cu.usbserial-1410", 9600)
ser.close()
ser.open()
 
fig, ax = plt.subplots(1,2, figsize  = (14,6))
 
while True:
                plt.ion()
                data = ser.readline().decode()
                d = pd.DataFrame([data.split(',')], columns = column_names)
                d = d.replace("\r\n", "", regex = True)
                df = df.append(d,  ignore_index = True)
                data = df.reset_index()
                data = data.rename(columns={'index': 'Time'})
                data = data.astype("float")
                print(data)
 
                sns.scatterplot(x = 'Time', y = 'Temperature (C)', color = 'red', data = data, ax = ax[0])
                sns.scatterplot(x = 'Time', y = "Humidity (%)", color = 'cyan', data = data, ax = ax[0])
                sns.scatterplot(x = 'Time', y = "Limunosity (lx)", color = 'lime', data = data, ax = ax[1])
                sns.scatterplot(x = 'Time', y = 'Noise (dB)', color = 'black', data = data, ax = ax[1])
                ax[0].set_ylabel("")
                ax[0].set_title("Temperature (C, red) and Humidity (%, blue)")
                ax[1].set_ylabel("")
                ax[1].set_title("Luminosity (lime, lx) and Noise (black, dB)")
                ax[0].set_ylim(10,70)
                # ax[1].set_ylim(10,400)
                plt.suptitle("Time Start: 20:20")
 
 
                plt.show()
                plt.pause(9)
 