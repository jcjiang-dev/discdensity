import numpy as np
import matplotlib.pyplot as plt

def density2(mlog,mdotlog,r_gravi,rin_gravi):
    sigma_t=6.64e-25
    unit=2 # 1 for rg, 2 for rs
    r=r_gravi/unit
    rin=rin_gravi/unit
    alpha=0.1
    xi=1
    f=0.0
    mlinear=np.power(10,mlog)
    mdotlinear=np.power(10,mdotlog)
    print(mlinear,mdotlinear)
    
    temp1=1/(sigma_t*2.95e5*mlinear)
    temp2=256*np.sqrt(2)/27
    temp3=np.power(alpha,-1.0)*np.power(r,3/2)*np.power(mdotlinear,-2)
    temp4=1-np.power(rin/r,1/2)
    temp5=xi*(1-f)
    ne=temp1*temp2*temp3*np.power(temp4,-2)*np.power(temp5,-3)
    return ne


mlog=7.0
mdotlog=np.linspace(-1.5,1.5,100)
rin_gravi=2 #in unit of gravitational radii
r_gravi=4 #in unit of gravitational radii

ne = density2(mlog, mdotlog, r_gravi, rin_gravi)

plt.figure(figsize=(8, 6))
plt.loglog(np.power(10,mdotlog*2+mlog), ne, label="ne vs. mdot", color="blue")
plt.xlabel(r"$m\dot{m}^2$", fontsize=14)
plt.ylabel(r"$n_e$ (cm$^{-3}$)", fontsize=14)
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend(fontsize=12)
plt.xlim(1e4,1e10)
plt.ylim(1e14,1e20)
plt.show()
