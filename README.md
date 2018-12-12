# Gated-Dipole-Reward-Circuit

By running `python run_sim.py`, the model will output multiple plots from a few different tests. The first test is a normal gated-dipole circuit and the resulting plot is the response from that circuit. The second test iterates over a modulated gated-dipole circuit that models addiction. The resulting plots include a plot of the response for the first application of the phasic input, for the last application of the phasic input, and for an application of the phasic input between the first and last. The second test also generates a histogram showing the occurence of phasic input applications for the given iteration over the model. This is necessary since applications of the phasic input are random and probability dependent. The final test creates 1000 instances of the modulated circuit and iterates over each until they reach addiction. The generated plot is a histogram from which the average number of iterations until addiction can be extrapolated.

## Install
`python setup.py install`
