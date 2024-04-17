import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Data
r1j1 = np.array([0.851, 0.894, 0.934, 1.081, 1.113])
r1j2 = np.array([0.755, 0.793, 0.914, 1.045, 1.212])
r1j3 = np.array([0.811, 0.821, 0.968, 1.11, 1.235])
log10conc = np.array([-7, -6, -5, -4, -3])

# Averaging
avgPeakResponse = np.log10((r1j1 + r1j2 + r1j3) / 3)

# Calculate standard deviation for error bars
std_dev = np.std([r1j1, r1j2, r1j3], axis=0)

# Interpolation
f = interp1d(log10conc, avgPeakResponse, kind='cubic')

# New points for smoother curve
new_log10conc = np.linspace(log10conc.min(), log10conc.max(), 500)
smoothed_curve = f(new_log10conc)

# Plot
plt.errorbar(log10conc, avgPeakResponse, yerr=std_dev, fmt='o', label='data points', capsize=5)
plt.plot(new_log10conc, smoothed_curve, '-', label='fitted sigmoid curve')
plt.xlabel('log10([AVP])    ([AVP],M)')
plt.ylabel('log10(cAMP) peak response   (arb. units)')

plt.grid(True)
plt.show()
