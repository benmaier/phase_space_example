#!/usr/bin/python
# -*- coding: utf-8 -*-

# import for fast numerics
import numpy as np

# import the routine for ODE integration
from scipy.integrate import ode

# import the plotting routines
import matplotlib.pyplot as pl

# set equation of motion for Lotka-Volterra (LV)
def dy_over_dt(t,y,a,b,c,d):

    R = y[0]
    F = y[1]

    result = np.zeros_like(y)

    result[0] = a*R - b*R*F
    result[1] = c*R*F - d*F

    return result

# set some parameters of the Lotka-Volterra (LV)
a = 2.0/3.0
b = 4.0/3.0
c = 1.0
d = 1.0

# initial values
R_0 = 1.0 # initial amount of Rabbits
F_0 = 1.0 # initial amount of Foxes
t_0 = 0.0 # initial time

# initial y-vector from initial values
y0 = np.array([R_0,F_0]) 

# initialize integrator
r = ode(dy_over_dt)

# Runge-Kutta with step size control
r.set_integrator('dopri5')

# set initial values
r.set_initial_value(y0,t_0)

# set LV-parameters to pass to dx/dt
r.set_f_params(a,b,c,d)

# max value of time and points in time to integrate to
t_max = 20
N_spacing_in_t = 1000

# create vector of time points you want to evaluate
t = np.linspace(t_0,t_max,N_spacing_in_t)

# create vector of positions for those times
y_result = np.zeros((len(t), 2))

# loop through all demanded time points
for it, t_ in enumerate(t):

    # get result of ODE integration up to the demanded time
    y = r.integrate(t_)

    # write result to result vector
    y_result[it,:] = y

# get angle and angular momentum
rabbits = y_result[:,0]
foxes = y_result[:,1]

# plot result
pl.plot(rabbits, foxes,'-',lw=1)
pl.xlabel('amount of rabbits $R$')
pl.ylabel('amount of foxes $F$')
pl.title('phase space')
pl.gcf().savefig('rabbits_foxes_phase_space.png',dpi=300)

pl.figure()
pl.plot(t, rabbits, label='rabbits')
pl.plot(t, foxes, label='foxes')
pl.xlabel('time $t$')
pl.ylabel('amount of species')
pl.legend()
pl.gcf().savefig('rabbits_foxes_trajectories.png',dpi=300)


pl.show()
