#!/usr/bin/python
# -*- coding: utf-8 -*-

# import for fast numerics
import numpy as np

# import the routine for ODE integration
from scipy.integrate import ode

# import the plotting routines
import matplotlib.pyplot as pl

# set equation of motion for pendulum
def dy_over_dt(t,y,g,l):
    r"""pendulum:

         d^2 x / dt^2 = - g/l * sin(x)
        where x is the angle of the pendulum
        
        in phase space:
        dx/dt = v
        dv/dt = (-g/l) sin(x)

        as vector equation
         d   / x \     /   0  1 \    /sin(x)\    dy
        --- |     | = |          |  |        | = --
        d t  \ v /     \ -g/l 0 /    \  v   /    dt
    """

    result = np.zeros_like(y)
    result[0] = y[1]
    result[1] = -g/l * np.sin(y[0])

    return result

# set parameters of pendulum
g = 1 # gravitational constant
l = 1 # pendulum length

# initial values
x_0 = 0 # intial angular position
v_0 = 1.0 # initial angular momentum
t_0 = 0 # initial time

# initial y-vector from initial position and momentum
y0 = np.array([x_0,v_0]) 

# initialize integrator
r = ode(dy_over_dt)

# Runge-Kutta with step size control
r.set_integrator('dopri5')

# set initial values
r.set_initial_value(y0,t_0)

# set g, l to pass to dx/dt
r.set_f_params(g,l)

# max value of time and points in time to integrate to
t_max = 10
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
angle = y_result[:,0]
angular_momentum = y_result[:,1]

# plot result
pl.plot(angle, angular_momentum,'-',lw=1)
pl.xlabel('angle $x$')
pl.ylabel('angular momentum $v$')

pl.gcf().savefig('pendulum_single_run.png',dpi=300)

pl.show()
