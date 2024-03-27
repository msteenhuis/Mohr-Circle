import numpy as np
import matplotlib.pyplot as plt
import math

###############################################################################
# Main Code

# Input variables (ONLY EDIT THIS PART)
S_x=100 #sigma_x
S_y=50 #sigma_y
tau_xy=20 # #tau_xy sign corresponding to shear stress associated with sigma_y plane


# Calculations
center = (S_x + S_y)/2.0
radius = np.sqrt((S_x - S_y)**2/4.0 + tau_xy**2)
S_min = center - radius
S_max = center + radius
tau_max = radius


# Plotting Purpose
# Axis plot
figure, axes = plt.subplots(1)
axes.axhline(y=0, color='k')
axes.axvline(x=0, color='k')

# Mohr Circle plot
circ = plt.Circle((center,0), radius, edgecolor='k', lw=1,facecolor='y') 

# Axis limits and labels
ax = plt.gca()
plt.xlabel(r"$\sigma$", size=18)
plt.ylabel(r"$\tau$", size=18)
ax.add_artist(circ)
ax.set_xlim(S_min - 0.5*radius, S_max + 0.5*radius)
ax.set_ylim(-1.5*radius, 1.5*radius)


# Relevant lines and points
plt.plot([S_y, S_x], [tau_xy, -tau_xy], 'ko')
plt.plot([S_y, S_y], [tau_xy, 0], '--k')
plt.plot([S_x, S_x], [-tau_xy, 0], '--k')
plt.plot([S_y, S_x], [tau_xy, -tau_xy], 'k')
plt.plot([center, center], [0, radius], '--b')
plt.gca().set_aspect('equal')
plt.plot(center, 0, 'o', mfc='k')

# Relevant Labels
plt.text(1.1*S_x, -tau_xy-np.sign(tau_xy)*0.25*radius, (S_x, -tau_xy),size=10,horizontalalignment='center')
plt.text(1.1*S_y, tau_xy+np.sign(tau_xy)*0.25*radius,(S_y, tau_xy) ,size=10,horizontalalignment='center')

# Principal stress and maximum in-plane shear stress location
plt.text(S_max+0.5*radius, 0.25*radius, '$\sigma_{max}$',size=15,horizontalalignment='right')
plt.text(S_min-0.5*radius, 0.25*radius, '$\sigma_{min}$',size=15,horizontalalignment='left')
plt.text(center, 1.45*radius, '$\\tau_{max}$',size=15,horizontalalignment='center',verticalalignment='top')

plt.text(S_max+0.4*radius, 0.05*radius, round(S_max,0),size=10,horizontalalignment='right')
plt.text(S_min-0.4*radius, 0.05*radius, round(S_min,0),size=10,horizontalalignment='left')
plt.text(center, 1.2*radius, round(radius,0),size=10,horizontalalignment='center',verticalalignment='top')


plt.title('Mohr Circle for 2D Plane Stress ');

plt.grid()


