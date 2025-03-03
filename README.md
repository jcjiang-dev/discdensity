# Disc densities in the standard $\alpha$ thin disc model

Disc Density Calculation Code (calculate_disc_density.py)
This code calculates the disc density at a given disc radius for a specified range of black hole masses and mass accretion rates.

## Key Parameters:
mlog: Logarithm of the black hole mass (in solar masses). This parameter can be a single value or an array of floating-point numbers.

mdotlog: Logarithm of the mass accretion rate, defined as: $\dot{m}=\lambda_{Edd}/\epsilon$, where $\lambda_{\rm Edd}$ is dimensionless Eddington ratio and $\epsilon$ is radiative efficiency. This parameter can also be an array of floating-point numbers.

rin_gravi: Inner radius of the disc, expressed in units of gravitational radii.

r_gravi: Disc radius at which the density is evaluated, also in units of gravitational radii.

f: Fraction of disc energy transferred to the corona.

## Model Assumptions:
This model does not include corrections for General Relativity and follows the formalism from Svensson & Zdziarski (1994), ApJ, 436, 599-606 for radiation pressure-dominated regions of the disc.

## Citing this Code:
If you use this code in your work, please cite the following references:

Svensson, R. & Zdziarski, A. A. (1994), Astrophysical Journal, 436, 599-606

https://ui.adsabs.harvard.edu/abs/1994ApJ...436..599S/abstract

Jiang, J., et al. (2019), Monthly Notices of the Royal Astronomical Society, 489(3), 3436-3455

https://ui.adsabs.harvard.edu/abs/2019MNRAS.489.3436J/abstract

Jiang, J., et al. (2019), Monthly Notices of the Royal Astronomical Society, 484(2), 1972-1982

https://ui.adsabs.harvard.edu/abs/2019MNRAS.484.1972J/abstract

# Previous disc density measurements using relativistic disc reflection models

An ASCII file containing an incomplete compilation of disc density measurements against their black hole mass and mass accretion rate. You may use this ASCII file to reproduce Fig. 5 in Liu et al. 2023.

If you use these measurements in your work, please cite the following papers.

https://ui.adsabs.harvard.edu/abs/2019MNRAS.484.1972J/abstract

https://ui.adsabs.harvard.edu/abs/2019MNRAS.489.3436J/abstract

https://ui.adsabs.harvard.edu/abs/2023ApJ...951..145L/abstract

https://ui.adsabs.harvard.edu/abs/2018ApJ...855....3T/abstract

https://ui.adsabs.harvard.edu/abs/2019MNRAS.483.2958J/abstract

https://ui.adsabs.harvard.edu/abs/2018MNRAS.479..615M/abstract

https://ui.adsabs.harvard.edu/abs/2019ApJ...871...88G/abstract

https://ui.adsabs.harvard.edu/abs/2018MNRAS.477.3711J/abstract
