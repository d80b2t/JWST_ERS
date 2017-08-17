# plot 5-10um data from Hill paper

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from math import *
import astropy.io.ascii as ascii 

data=ascii.read
data =  ascii.read('table2.txt')

wavelength = data['col1']
total      = data['col2']
most_lum = data['col3']
medium_lum = data['col4']
least_lum = data['col5']

fig1=plt.figure()
ax1=fig1.gca()
ax1.axis([5,10,0,1.7])
ax1.set_title('Quasar composites vs luminosity: data from Hill et 2014', size=16)
ax1.set_xlabel('Rest $\lambda$, microns', size=16)
ax1.set_ylabel('Relative flux', size=16)
ax1.tick_params(labelsize=16)

#ax1.plot(wavelength,total)
ax1.plot(wavelength,least_lum*1.3,lw=2)
ax1.plot(wavelength,most_lum/1.7,lw=2)
ax1.plot(wavelength,medium_lum,lw=2)


ax1.text(6.2,1.2,'PAH',size=16,ha='center')
ax1.text(7.7,1.6,'PAH',size=16,ha='center')
ax1.text(8.6,1.1,'PAH',size=16,ha='center')

ax1.text(6.97,0.95,'[ArIII]',size=16,ha='center')
ax1.text(8.97,0.95,'[ArIII]',size=16,ha='center')

plt.show()
