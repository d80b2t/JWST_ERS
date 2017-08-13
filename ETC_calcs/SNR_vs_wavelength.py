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
twenty =  ascii.read(path+'SNR_vs_wavelength_2866sec_20Gr03Ints.dat')
ten = ascii.read(path+'SNR_vs_wavelength_2866sec_10Gr06Ints.dat')
fife = ascii.read(path+'SNR_vs_wavelength_2150sec_15Gr03Ints.dat')

##
##  P l o t t i n g    t h i n g s    u p...
##
plt.rcParams.update({'font.size': 18})
fig, ax = plt.subplots(figsize=(16, 7))

plt.plot(twenty['Wavelength'], twenty['snr'], linestyle='solid', linewidth=4)
plt.plot(ten['Wavelength'], ten['snr'], linestyle='dotted', linewidth=4)
plt.plot(fife['Wavelength'], fife['snr'], linestyle='dashed', linewidth=4)

plt.legend(['2866sec_20Gr03Ints', '2866sec_10Gr06Ints', '2150sec_15Gr03Ints'], 
           loc="upper right", ncol=1, shadow=True, fancybox=True,
           fontsize=22, frameon=True)

plt.xlabel('wavelength / $\mu$m ')
plt.ylabel('ETC SNR')
plt.show()
fig.savefig("SNR_vs_wavelength_comparisons_temp.pdf")
plt.close(fig)




