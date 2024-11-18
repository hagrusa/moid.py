# if moid.f has been compiled into a shared object (i.e., moidpy.so)
# then you should be able to simply import the library
# so long as moidpy.so is in the same directory as this script or in your PYTHONPATH
import moidpy
import numpy as np

#orbital elements of Earth and Didymos taken from JPL Horizons
# #on 2024-01-01 w.r.t solar system barycenter
a_earth = 0.9951504164652991                #semimajor axis, au
e_earth = 0.0151391393004173				#eccentricity
i_earth = 0.009210993545298243 #inclination
w_earth = 57.43291446810953  #argument of pericenter
Omega_earth = 14.32664085927617 #longitude of ascending node


a_didy = 1.651360984551208
e_didy = 0.3812739081678559
i_didy = 3.410437379389624
w_didy = 319.3281724872755
Omega_didy = 72.92737351585056


moid = moidpy.moid_func(a_earth, e_earth, i_earth, w_earth, Omega_earth,
						a_didy,  e_didy,  i_didy,  w_didy,  Omega_didy)
print(f"Earth-Didymos MOID: {moid} au")


# from astroquery.jplhorizons import Horizons
# epoch={'start':'2024-01-01', 'stop':'2024-01-02', 'step':'10d'} #just want a single epoch
# earth = Horizons(id=3,location='ssb', epochs=epoch).elements()
# didymos = Horizons(id="Didymos",location='ssb', epochs=epoch, id_type='smallbody').elements() 
# moid = moidpy.moid_func(earth['a'], earth['e'], earth['incl'], earth['w'], earth['Omega'],
# 							  didymos['a'], didymos['e'], didymos['incl'], didymos['w'], didymos['Omega'])
# print(f"Earth-Didymos MOID: {moid} au")




