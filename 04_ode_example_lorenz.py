#!/usr/bin/python
# -*- coding: utf-8 -*-

# import for fast numerics
import numpy as np

# import the routine for ODE integration
from scipy.integrate import ode

# import the plotting routines
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D

# set equation of motion for Lorenz system
def dL_over_dt(t,L,sigma,rho,beta):

    x = L[0]
    y = L[1]
    z = L[2]

    result = np.zeros_like(L)

    result[0] = sigma*(y-x)
    result[1] = x * (rho-z) - y
    result[2] = x*y - beta*z

    return result

# set some parameters of the Lorenz system
sigma = 10.0
rhos = [9.0, 160.0, 28.0 ] 
beta = 8./3.0

# initial values
x_0 = 10.0 # initial amount of Rabbits
y_0 = 10.0 # initial amount of Foxes
z_0 = 10.0 # initial time
t_0 = 1.0

# initial y-vector from initial values
L0 = np.array([x_0, y_0, z_0]) 

fig = pl.figure(figsize=(12,6))

for irho, rho in enumerate(rhos):

    # initialize integrator
    r = ode(dL_over_dt)

    # Runge-Kutta with step size control
    r.set_integrator('dopri5')

    # set initial values
    r.set_initial_value(L0,t_0)

    # set LV-parameters to pass to dx/dt
    r.set_f_params(sigma, rho, beta)

    # max value of time and points in time to integrate to
    t_max = 20
    N_spacing_in_t = 10000

    # create vector of time points you want to evaluate
    t = np.linspace(t_0,t_max,N_spacing_in_t)

    # create vector of positions for those times
    L_result = np.zeros((len(t), 3))

    # loop through all demanded time points
    for it, t_ in enumerate(t):

        # get result of ODE integration up to the demanded time
        L = r.integrate(t_)

        # write result to result vector
        L_result[it,:] = L

    # get angle and angular momentum
    x = L_result[:,0]
    y = L_result[:,1]
    z = L_result[:,2]

    # get indices where t>3 to ignore transient dynamics 
    ndx = np.where(t>3)

    # create 3d-figure
    ax3d = fig.add_subplot('23'+str(irho+1),projection='3d')
    ax3d.plot(x[ndx],y[ndx],z[ndx],lw=0.5)
    ax3d.set_title(r'$\rho={0:d}$'.format(int(rho)))
    ax3d.set_xlabel('x')
    ax3d.set_ylabel('y')
    ax3d.set_zlabel('z')

    ax2d = fig.add_subplot('23'+str(4+irho))


    ax2d.plot(t, x, label='x',lw=1.)
    ax2d.plot(t, y, label='y',lw=1.)
    ax2d.plot(t, z, label='z',lw=1.)
    ax2d.set_xlabel('time $t$')
    ax2d.set_ylabel('values')
    ax2d.legend()


fig.tight_layout()
fig.savefig('lorenz.png',dpi=300)
pl.show()
