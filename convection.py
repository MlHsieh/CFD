"""
CFD written in python following the guide "CFD Python: 12 steps to Navier-Stokes"
https://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/
"""

import sys, time
import numpy as np
import matplotlib.pyplot as plt

def linear_convection(nx):
    """
    1-D linear convection
    nx: number of grids
    """
    dx = 2/(nx-1)
    nt = 25
    c = 1       # speed of wave
    sigma = 0.5
    dt = sigma*dx

    u = np.ones(nx)
    u[int(0.5/dx):int(1/dx + 1)] = 2    # initial conditions: u = 2 at x = [0.5, 1]

    un = np.ones(nx) #initialize a temporary array

    for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
        un = u.copy() ##copy the existing values of u into un
        for i in range(1, nx):
            u[i] = un[i] - c*dt/dx*(un[i]-un[i-1])

    # plot the wave shape
    plt.plot(np.linspace(0, 2, nx), u)
    plt.show()


if __name__ == "__main__":
    np.seterr('raise')
    linear_convection(91)
