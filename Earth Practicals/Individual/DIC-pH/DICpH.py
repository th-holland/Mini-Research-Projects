import numpy as np
import matplotlib.pyplot as plt

# import package for Ka values 
##### ALL VALUES:
## TEMP deg C

def deltaCO2(_deltaT, _pCO2):
    return 0.0423 * _deltaT * _pCO2

def dCO2dt(_CO2, _k1, _H, _HCO3):
    return -_k1 * _CO2 + 1/_k1 * _H * _HCO3

def dHdt(_CO2, _k1, _H, _HCO3, _k2, _CO3):
    return _k1 * _CO2 - 1/_k1 * _H * _HCO3 + _k2 * _HCO3 - 1/_k2 * _H * _CO3

def dHCO3dt(_CO2, _k1, _H, _HCO3, _k2, _CO3):
    return _k1 * _CO2 - 1/_k1 * _H * _HCO3 - _k2 * _HCO3 + 1/_k2 * _H * _CO3

def dCO3dt(_k2, _H, _CO3):
    return _k2 * _H - 1/_k2 * _H * _CO3


def model(_params):
    # initial conditions
    CO2 = _params['pCO2']
    H = _params['H']
    HCO3 = _params['HCO3']
    CO3 = _params['CO3']
    k1 = _params['k1']
    k2 = _params['k2']
    dt = _params['dt']
    time = _params['time']
    years = _params['years']
    pCO2 = _params['pCO2']
    deltaT = _params['dt']
    # generate model
    CO2_model = np.zeros(len(time))
    H_model = np.zeros(len(time))
    HCO3_model = np.zeros(len(time))
    CO3_model = np.zeros(len(time))
    for i in range(len(time)):
        CO2_model[i] = CO2
        H_model[i] = H
        HCO3_model[i] = HCO3
        CO3_model[i] = CO3
        CO2 += dCO2dt(CO2, k1, H, HCO3) * dt
        H += dHdt(CO2, k1, H, HCO3, k2, CO3) * dt
        HCO3 += dHCO3dt(CO2, k1, H, HCO3, k2, CO3) * dt
        CO3 += dCO3dt(k2, H, CO3) * dt
    return CO2_model, H_model, HCO3_model, CO3_model