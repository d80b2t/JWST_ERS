'''
Characterizing quasars in the mid-infrared: high signal-to-noise ratio spectral templates 
Allison R. Hill  S. C. Gallagher  R. P. Deo  E. Peeters  Gordon T. Richards
Monthly Notices of the Royal Astronomical Society, Volume 438, Issue 3, 1 March 2014, Pages 2317–2327, https://doi.org/10.1093/mnras/stt2346
Published: 31 December 2013  Article history
'''

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from astropy.io import ascii

path = '/cos_pc19a_npr/data/Spitzer/Hill2014_IRS/'

##
##  P h o t o m e t r y    d a t a
##
data =  ascii.read(path+'table2.txt')
##data =  ascii.read('table2.txt')

wavelength = data['col1']
total      = data['col2']
most_lum = data['col3']
medium_lum = data['col4']
least_lum = data['col5']


'''
#Table 2 of Allison R. Hill et al (2013)
#This table contains the values for the templates generated from the objects listed in Table 1. Entries which contain a '-1' indicate no wavelength coverage for that template.
#col 1: wavelength [micron]
#col 2: total template (spectral average of all objects) in units of L_{nu}
#col 3,4,5: the most luminous, intermediate luminosity and least luminous template (corresponding to values 1, 2 and 3 from col 10 of Table 1) in units if L_{nu}
#
#
'''

##
##  P l o t t i n g    t h i n g s    u p...
##
plt.rcParams.update({'font.size': 20})
fig, ax = plt.subplots(figsize=(10, 7))

ax = plt.gca()
ax.get_xaxis().set_tick_params(which='both', direction='in')
ax.get_yaxis().set_tick_params(which='both', direction='in')

#plt.plot(wavelength, total+2, linestyle='solid', linewidth=4, color='b')
#plt.plot(wavelength, least_lum+4, linestyle='dashed', linewidth=4)
#plt.plot(wavelength, medium_lum+6, linestyle='dotted', linewidth=4)
#plt.plot(wavelength, most_lum+8, linestyle='dashdot', linewidth=4)

#plt.plot(wavelength, total, linestyle='solid', linewidth=4, color='b')
plt.plot(wavelength, least_lum*2.6, linestyle='solid', linewidth=4)
plt.plot(wavelength, medium_lum*2.2, linestyle='dotted', linewidth=4)
plt.plot(wavelength, most_lum*1.25, linestyle='dashed', linewidth=4)
#plt.legend(['log(L_{5.6 $\mu$m}) < 43 erg s^{−1}',
 #           '43.6 < log(L_{5.6 $\mu$m}) < 44.7',
  #          '44.8 < log(L_{5.6 $\mu$m}) < 46.1'], 
#           loc="upper left", ncol=1, shadow=True, fancybox=True,
   #        loc="upper right", ncol=1, shadow=True, fancybox=True,
    #       fontsize=20, frameon=True)

ymax = 3.5
ax.text(6.2,ymax*0.70,'PAH',size=16,ha='center')
ax.text(7.5,ymax*0.90,'PAH',size=16,ha='center')
ax.text(8.6,ymax*0.65,'PAH',size=16,ha='center')

ax.text(6.7,ymax*0.50,'[ArII]',size=16,ha='center')
ax.text(7.2,ymax*0.65,'[Ne VI]',size=16,ha='center')
#ax.text(8.97,0.95,'[ArII]',size=16,ha='center')

    
#@plt.ylim([0,10])
#plt.xlim([5.0,10])
plt.xlim([4.9,9.0])
plt.ylim([0.2,ymax])
#ax1.axis([5,10, 0, 1.7])

plt.xlabel('Rest wavelength / $\mu$m ', size=20)
#plt.xlabel('Rest $\lambda$, microns')
#ax1.set_ylabel('Relative flux', size=16)
plt.ylabel('Relative flux', size=20)
#plt.ylabel('Luminosity_{\nu} [normalized]')

plt.show()
fig.savefig("Hill2014_IRspectra_Lrange_temp.pdf")
plt.close(fig)




