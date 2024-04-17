import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Sigmoid function
def sigmoid(x, a, b, c, d):
    return a / (1 + np.exp(-b * (x - c))) + d

# Data
nr = 6
r1j1 = np.array([22536, 23300, 22054, 9658, 1234, 366, 246, 246, 266])
r1j2 = np.array([22890, 24571, 22124, 10290, 1298, 366, 266, 268, 256])
r1j3 = np.array([15777, 17005, 14963, 4728, 744, 312, 308, 314, 284])
r1j4 = np.array([16565, 18347, 18171, 5372, 804, 374, 336, 360, 328])
r1j5 = np.array([14655, 15903, 16745, 16259, 7788, 648, 184, 172, 158])
r1j6 = np.array([16003, 17315, 17895, 17821, 8608, 798, 216, 208, 184])

log10conc = np.array([-6, -7, -8, -9, -10, -11, -12, -13, -14])

log10r1j1 = np.log10(r1j1)
log10r1j2 = np.log10(r1j2)
log10r1j3 = np.log10(r1j3)
log10r1j4 = np.log10(r1j4)
log10r1j5 = np.log10(r1j5)
log10r1j6 = np.log10(r1j6)

aver = (log10r1j1 + log10r1j2 + log10r1j3 + log10r1j4 + log10r1j5 + log10r1j6) / nr

# Averaging
avgPeakResponse = (aver)

# Calculate standard deviation for each data point
std_dev = np.std([log10r1j1, log10r1j2, log10r1j3, log10r1j4, log10r1j5, log10r1j6], axis=0)

# Fit sigmoid curve
p0 = [max(avgPeakResponse), 1, np.median(log10conc), min(avgPeakResponse)]  # Initial guess for the parameters
popt, pcov = curve_fit(sigmoid, log10conc, avgPeakResponse, p0=p0)

# Generate denser set of points for smoother curve
new_log10conc = np.linspace(log10conc.min(), log10conc.max(), 1000)
smoothed_curve = sigmoid(new_log10conc, *popt)

# Plot
plt.plot(new_log10conc, smoothed_curve, '-', label='Fitted Sigmoid Curve')
plt.scatter(log10conc, avgPeakResponse, marker='o', color='red', label='Data Points')  # Data points
plt.errorbar(log10conc, avgPeakResponse, yerr=std_dev, fmt='none', color='black', capsize=5, capthick=2, label='Error Bars')  # Vertical error bars
plt.xlabel('log10([AVP])    ([AVP],M)')
plt.ylabel('log10(cAMP) peak response   (arb. units)')

plt.grid(True)
plt.legend()
plt.show()
