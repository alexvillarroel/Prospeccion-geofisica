from obspy.core import read
import numpy as np
import matplotlib.pyplot as plt
data1=read('/home/alex/Desktop/Prospeccion-geofisica/Cert1/1.dat')
data2=read('/home/alex/Desktop/Prospeccion-geofisica/Cert1/10.dat')
data1_copy=data1
data2_copy=data2
for i in range(0,24):
    data1[i].plot()
