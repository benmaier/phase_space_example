# How to: Integrate ODEs and plot trajectories in phase space


This is a small collection of Python scripts which illustrate how to integrate ODEs in Python and
how to plot trajectories in phase space. 

# Access

Either clone this repository as 

    git clone git@github.com:benmaier/phase_space_example.git 

or [download a zip-file](https://github.com/benmaier/phase_space_example/archive/master.zip).

# Content

As an illustration example, you could begin with a [simple pendulum](https://bit.ly/2N5azyx). In
[`01_ode_example_pendulum.py`](https://github.com/benmaier/phase_space_example/blob/master/01_ode_example_pendulum.py), 
I illustrated how to write down the equations of motion as a function
and then integrated it to obtain a limit cycle in phase space.

![pendulum-single-run](https://github.com/benmaier/phase_space_example/raw/master/pendulum_single_run.png)

In [`02_scan_pendulum.py`](https://github.com/benmaier/phase_space_example/blob/master/02_scan_pendulum.py) 
I added a few lines of code to illustrate how one would scan different
initial conditions and parameters to see how the trajectories change.

![pendulum-scan](https://github.com/benmaier/phase_space_example/raw/master/pendulum_scan.png)

In [`03_ode_example_lotka_volterra.py`](https://github.com/benmaier/phase_space_example/blob/master/03_ode_example_lotka_volterra.py), 
I show how to integrate a [Lotka-Volterra system](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) and how
to plot both the time evolution as well as the phase space trajectory.

![lotka-volterra](https://github.com/benmaier/phase_space_example/raw/master/rabbits_foxes_phase_space.png)

![lotka-volterra-2](https://github.com/benmaier/phase_space_example/raw/master/rabbits_foxes_trajectories.png)

Finally, in [`04_ode_example_lorenz.py`](https://github.com/benmaier/phase_space_example/blob/master/04_ode_example_lorenz.py),
I replicated the figures from Dave's lecture for the [Lorenz system](https://en.wikipedia.org/wiki/Lorenz_system).
Playing around with this system is the most fun because it shows chaotic behavior.


![lorenz](https://github.com/benmaier/phase_space_example/raw/master/lorenz.png)
