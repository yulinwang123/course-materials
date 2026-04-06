from numba.pycc import CC
from numba import vectorize, jit, prange
import numpy as np

@jit(nopython=True)
def distance_jit(lon1, lat1, lon2, lat2):
    '''
    Calculate the circle distance between two points
    on the earth (specified in decimal degrees)
    '''
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = np.radians([lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    # 6367 km is the radius of the Earth
    km = 6367 * c
    m = km * 1000
    return m


cc = CC('aot')
@cc.export('distance', 'f8(f8,f8,f8,f8)')
@cc.export('distance_v', 'f8[:](f8[:],f8[:],f8,f8)')
def distance_numba(lon1, lat1, lon2, lat2):
    '''                                                                         
    Calculate the circle distance between two points                            
    on the earth (specified in decimal degrees)
    
    (distance: Numba-accelerated; distance_v: Numba-accelerated + vectorized)
    '''
    # convert decimal degrees to radians                        
    lon1, lat1 = map(np.radians, [lon1, lat1])
    lon2, lat2 = map(np.radians, [lon2, lat2])

    # haversine formula                                                         
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    # 6367 km is the radius of the Earth                                        
    km = 6367 * c
    m = km * 1000
    return m
cc.compile()