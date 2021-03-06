#!/usr/bin/env python3
import matplotlib.pyplot as plt
from numpy import genfromtxt,arange  
Ex=genfromtxt("field-evol-Ex.dat")
Ex=Ex[:,1]
Ey=genfromtxt("field-evol-Ey.dat")
Ey=Ey[:,1]
Bz=genfromtxt("field-evol-Bz.dat")
Bz=Bz[:,1]
arg=arange(len(Ey))
plt.plot(arg,Ex,label="$E_x$")
plt.plot(arg,Ey,label="$E_y$")
plt.plot(arg,Bz,label="$B_z$")
plt.xlabel("x")
plt.legend()
#plt.savefig("field-evol-simple.pdf")
plt.show()
