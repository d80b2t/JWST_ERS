'''
Some cute unit/flux density luminosity conversions
    http://www.astro.soton.ac.uk/~td/flux_convert.html
            (Janskys to Watts)     * (4.pi.R^2)      * (freq in Hz) *     
IDL> print, ((2351.50*1e-6)*1e-26) * (5.2952985d+51) * (83333e9)    *(1e7)
'''

import math 
import numpy as np

w4mpro = float(input("The WISE W4 magnitude??:  "))

## http://wise2.ipac.caltech.edu/docs/release/allsky/expsup/sec4_4h.html#Summary
Flux_nu_0_W1  = 309.540
Flux_nu_0_W2  = 171.787
Flux_nu_0_W3  =  31.674
Flux_nu_0_W4  =   8.363


#Flux_nu_W1_Jy  = Flux_nu_0_W1 * (10**(-1.*(data.w1mpro)/2.5))
#Flux_nu_W1_uJy = Flux_nu_W1_Jy*1e6

Flux_nu_W4_Jy  = Flux_nu_0_W4 * (10**(-1.*(w4mpro)/2.5))
Flux_nu_W4_mJy = Flux_nu_W4_Jy*1e3
#Flux_nu_W4_uJy = Flux_nu_W4_Jy*1e6

print('WISE W4 flux in  Jy', Flux_nu_W4_Jy)
print('WISE W4 flux in mJy', Flux_nu_W4_mJy)



