import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define numpy arrays
r0 = np.array([172, 188, 210, 204, 270, 260, 266, 278, 232, 262, 228, 252, 238,
               248, 236, 256, 240, 234, 240, 232, 216, 238, 210, 194, 218, 182,
               182, 176, 180, 174])
r7 = np.array([456, 942, 1362, 1724, 2108, 2312, 2446, 2670, 2690, 2754, 2746,
               2742, 2772, 2738, 2712, 2660, 2612, 2580, 2558, 2474, 2548, 2362,
               2346, 2342, 2226, 2194, 2164, 2058, 2124, 1988])
r6 = np.array([714, 1144, 1628, 1892, 2264, 2382, 2508, 2676, 2702, 2796, 2744,
               2826, 2724, 2580, 2690, 2548, 2556, 2602, 2538, 2432, 2394, 2434,
               2308, 2326, 2258, 2262, 2094, 2244, 2192, 2196])
r10 = np.array([238, 440, 716, 940, 1284, 1518, 1778, 1988, 2118, 2306, 2450,
                2502, 2452, 2674, 2696, 2632, 2562, 2680, 2564, 2542, 2458, 2528,
                2398, 2332, 2278, 2306, 2236, 2166, 2178, 2152])
r9 = np.array([286, 722, 1276, 1808, 2248, 2668, 2922, 3114, 3308, 3358, 3442,
               3592, 3644, 3698, 3586, 3678, 3544, 3544, 3530, 3582, 3588, 3504,
               3384, 3344, 3206, 3194, 3244, 3174, 3054, 3156])
r8 = np.array([426, 970, 1576, 1958, 2260, 2550, 2666, 2908, 2902, 3088, 3038,
               2996, 3114, 3104, 2948, 3078, 3004, 2992, 2908, 2918, 2902, 2804,
               2670, 2744, 2586, 2542, 2524, 2486, 2446, 2400])
r11 = np.array([224, 282, 352, 434, 580, 624, 732, 766, 794, 900, 946,
                1006, 992, 984, 968, 984, 1006, 1016, 972, 1004, 994, 958,
                864, 878, 818, 840, 896, 754, 766, 750])
r12 = np.array([150, 176, 256, 258, 326, 356, 360, 440, 452, 432, 492, 456, 476,
                496, 516, 500, 494, 406, 496, 424, 454, 426, 390, 424, 386, 398,
                370, 378, 356, 364])
r13 = np.array([160, 206, 228, 224, 270, 272, 274, 312, 344, 294, 312, 308, 314,
                306, 344, 334, 328, 274, 286, 300, 284, 268, 252, 250, 250, 222,
                270, 242, 246, 240])

# Time points
time = np.arange(0, len(r0))

# Define curve fitting function (using a polynomial function)
def func(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Fit curves and plot
plt.figure(figsize=(10, 6))

plt.plot(time, r0, marker='o', linestyle='none', label='10⁻¹⁴ M')
popt, pcov = curve_fit(func, time, r0)
plt.plot(time, func(time, *popt), 'r--')

plt.plot(time, r7, marker='s', linestyle='none', label='10⁻⁷ M')
popt, pcov = curve_fit(func, time, r7)
plt.plot(time, func(time, *popt), 'g--')

plt.plot(time, r6, marker='^', linestyle='none', label='10⁻⁶ M')
popt, pcov = curve_fit(func, time, r6)
plt.plot(time, func(time, *popt), 'b--')

plt.plot(time, r10, marker='x', linestyle='none', label='10⁻¹⁰ M')
popt, pcov = curve_fit(func, time, r10)
plt.plot(time, func(time, *popt), 'c--')

plt.plot(time, r9, marker='D', linestyle='none', label='10⁻⁹ M')
popt, pcov = curve_fit(func, time, r9)
plt.plot(time, func(time, *popt), 'm--')

plt.plot(time, r8, marker='o', linestyle='none', label='10⁻⁸ M')
popt, pcov = curve_fit(func, time, r8)
plt.plot(time, func(time, *popt), 'y--')

plt.plot(time, r11, marker='s', linestyle='none', label='10⁻¹¹ M')
popt, pcov = curve_fit(func, time, r11)
plt.plot(time, func(time, *popt), 'k--')

plt.plot(time, r12, marker='^', linestyle='none', label='10⁻¹² M')
popt, pcov = curve_fit(func, time, r12)
plt.plot(time, func(time, *popt), 'r--')

plt.plot(time, r13, marker='x', linestyle='none', label='10⁻¹³ M')
popt, pcov = curve_fit(func, time, r13)
plt.plot(time, func(time, *popt), 'g--')

plt.xlabel('repeats',fontsize=20)
plt.ylabel('cAMP Response',fontsize=20)

plt.legend()
plt.grid(True)
plt.show()