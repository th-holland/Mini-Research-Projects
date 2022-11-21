import matplotlib.pyplot as plt
import numpy as np
from DICpH import model
from math import exp

# initial conditions

# CO2 = 414.72 ppm

params = {
    'pCO2': 0.041472,
    'H': 10**-7.0,
    'HCO3': 0,
    'CO3': 0,
    'k1': 10**-6.3,
    'k2': 10**-10.3,
    'dt': 0.1,
    'years': 100,
    'time': 0
}

# calculate time array
params['time'] = np.arange(0, params['years'], params['dt'])

print(params['time'])

# run model

CO2_model, H_model, HCO3_model, CO3_model = model(params)

# print model in table of every 10 years

for i in range(0, len(params['time']), 100):
    print('Year: ', params['time'][i], 'CO2: ', CO2_model[i], 'H: ', H_model[i], 'HCO3: ', HCO3_model[i], 'CO3: ', CO3_model[i])

## convert all to log scale

H_model = np.log10(H_model)
HCO3_model = np.log10(HCO3_model)
CO3_model = np.log10(CO3_model)
C02_model = np.log10(CO2_model)

# plot model

plt.plot(params['time'], H_model, label='H')
plt.plot(params['time'], HCO3_model, label='HCO3')
plt.plot(params['time'], CO3_model, label='CO3')
plt.plot(params['time'], CO2_model, label='CO2')
plt.xlim(0, 100)
plt.legend()
plt.show()

