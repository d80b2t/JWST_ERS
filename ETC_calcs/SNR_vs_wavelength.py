'''
The IFU Nod-in-scene vs IFU nod-off-scene strategies are described in
the JWST ETC Documentation article:
https://jwst-docs.stsci.edu/display/JPP/JWST+ETC+IFU+Nod+in+Scene+and+IFU+Nod+off+Scene+Strategy

Groups/integrations/exposures: The main thing to know is that
increasing Ngroups increases reads and therefore readnoise, whereas
integrations and exposures do not. We suggest that you use two batch
expansions, one over groups and one over integrations, to get a feel
for how the SNR(time) slope changes with each

4 Point Dither: As you observe, the IFU nod-in-scene strategy uses a 2
point dither, so you should specify an additional 2 exposures to get
the equivalent of a 4 point dither.
'''

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from astropy.io import ascii


path = '/cos_pc19a_npr/LaTeX/proposals/JWST/JWST_ERS/ETC_calcs/'


##
##  P h o t o m e t r y    d a t a
##
twenty_three =  ascii.read(path+'SNR_vs_wavelength_2866sec_20Gr03Ints.dat')
#twenty_six =  ascii.read(path+'SNR_vs_wavelength_2866sec_20Gr06Ints.dat')
ten_three = ascii.read(path+'SNR_vs_wavelength_1433sec_10Gr03Ints.dat')
ten_six = ascii.read(path+'SNR_vs_wavelength_2866sec_10Gr06Ints.dat')
fife_three = ascii.read(path+'SNR_vs_wavelength_2150sec_15Gr03Ints.dat')
fife_six = ascii.read(path+'SNR_vs_wavelength_4300sec_15Gr06Ints.dat')

fortyfive = ascii.read(path+'SNR_vs_wavelength_2150sec_45Gr01Ints.dat')
twentytwo_two = ascii.read(path+'SNR_vs_wavelength_2102sec_22Gr02Ints.dat')
eleven_four = ascii.read(path+'SNR_vs_wavelength_2102sec_11Gr04Ints.dat')



##
##  P l o t t i n g    t h i n g s    u p...
##
plt.rcParams.update({'font.size': 20})
fig, ax = plt.subplots(figsize=(16, 7))

ax = plt.gca()
ax.get_xaxis().set_tick_params(which='both', direction='in')
ax.get_yaxis().set_tick_params(which='both', direction='in')


'''
plt.plot(twenty_three['Wavelength'], twenty_three['snr'], linestyle='solid', linewidth=4)
plt.plot(ten_three['Wavelength'], ten_three['snr'], linestyle='dotted', linewidth=4)
plt.plot(fife_three['Wavelength'], fife_three['snr'], linestyle='dashed', linewidth=4)
plt.plot(ten_six['Wavelength'], ten_six['snr'], linestyle='dotted', linewidth=4)
#plt.plot(fife_six['Wavelength'], fife_six['snr'], linestyle='dashed', linewidth=4)

plt.legend(['2866sec_20Gr03Ints', '1433sec_10Gr03Ints', '2150sec_15Gr03Ints', '2866sec_10Gr06Ints'], 
           loc="upper right", ncol=1, shadow=True, fancybox=True,
           fontsize=22, frameon=True)
'''
'''
plt.plot(fortyfive['Wavelength'], fortyfive['snr'], linestyle='solid', linewidth=4)
plt.plot(twentytwo_two['Wavelength'], twentytwo_two['snr'], linestyle='dotted', linewidth=4)
plt.plot(fife_three['Wavelength'], fife_three['snr'], linestyle='dashed', linewidth=4)
plt.plot(eleven_four['Wavelength'], eleven_four['snr'], linestyle='dashdot', linewidth=4)

plt.legend(['2150sec_45Gr01Ints', '2102sec_22Gr02Ints', '2150sec_15Gr03Ints', '2102sec_11Gr04Ints' ], 
           loc="upper right", ncol=1, shadow=True, fancybox=True,
           fontsize=22, frameon=True)
'''

plt.plot(fife_six['Wavelength'], fife_six['snr'], linestyle='dashdot', linewidth=4)
plt.plot(twenty_three['Wavelength'], twenty_three['snr'], linestyle='solid', linewidth=4)
plt.plot(ten_six['Wavelength'], ten_six['snr'], linestyle='solid', linewidth=4)

plt.plot(fortyfive['Wavelength'], fortyfive['snr'], linestyle='dashed', linewidth=4)
plt.plot(fife_three['Wavelength'], fife_three['snr'], linestyle='dashed', linewidth=4)

plt.plot(twentytwo_two['Wavelength'], twentytwo_two['snr'], linestyle='dotted', linewidth=4)
plt.plot(eleven_four['Wavelength'], eleven_four['snr'], linestyle='dotted', linewidth=4)

plt.plot(ten_three['Wavelength'], ten_three['snr'], linestyle='dashdot', linewidth=4)

plt.legend(['4300sec  15Gr06Ints', '2866sec  20Gr03Ints', '2866sec  10Gr06Ints', '2150sec  45Gr01Ints', 
            '2150sec  15Gr03Ints', '2102sec  22Gr02Ints', '2102sec  11Gr04Ints', '1433sec  10Gr03Ints'], 
           loc="upper right", ncol=1, shadow=True, fancybox=True,
           fontsize=20, frameon=True)



plt.ylim([0,140])

plt.xlabel('wavelength / $\mu$m ')
plt.ylabel('ETC SNR')
plt.show()
fig.savefig("SNR_vs_wavelength_comparisons_temp.pdf")
plt.close(fig)




