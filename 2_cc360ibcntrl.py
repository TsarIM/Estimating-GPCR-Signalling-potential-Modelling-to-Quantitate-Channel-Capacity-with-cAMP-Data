import numpy as np
from scipy.integrate import quad
from scipy.optimize import linprog

def Func_dr(x, sigma, aver, i):

    p_c_r = lambda sig, av, x: (1 / (sig * np.sqrt(2 * np.pi))) * np.exp(-((x - av) ** 2) / (2 * sig ** 2))
    
    p_c_r_i = lambda x: p_c_r(sigma[i], aver[i], x)

    p_r = lambda x: np.mean([p_c_r(sig, av, x) for sig, av in zip(sigma, aver)])

    fdr = lambda x: p_c_r_i(x) * (np.log2(p_c_r_i(x) / p_r(x)))

    return fdr(x)

def integrate_fdr(sigma, aver, i, lower_limit, upper_limit):

    integrand = lambda x: Func_dr(x, sigma, aver, i)

    result, _ = quad(integrand, lower_limit, upper_limit)

    return result

integral1 = []

nr=6
r1j1 = np.array([22536, 23300, 22054, 9658, 1234, 366, 246, 246, 266])
r1j2 = np.array([22890, 24571, 22124, 10290, 1298, 366, 266, 268, 256])
r1j3 = np.array([15777, 17005, 14963, 4728, 744, 312, 308, 314, 284])
r1j4 = np.array([16565, 18347, 18171, 5372, 804, 374, 336, 360, 328])
r1j5 = np.array([14655, 15903, 16745, 16259, 7788, 648, 184, 172, 158])
r1j6 = np.array([16003, 17315, 17895, 17821, 8608, 798, 216, 208, 184])

# conc= np.array([-6, -7, -8, -9, -10, -11, -12, -13, -14])

log10r1j1=np.log10(r1j1)

log10r1j2=np.log10(r1j2)

log10r1j3=np.log10(r1j3)

log10r1j4=np.log10(r1j4)

log10r1j5=np.log10(r1j5)

log10r1j6=np.log10(r1j6)



aver=(log10r1j1+log10r1j2+log10r1j3+log10r1j4+log10r1j5+log10r1j6)/nr

sigma = np.std([log10r1j1,log10r1j2,log10r1j3,log10r1j4,log10r1j5,log10r1j6], axis=0)

# Calculate channel capacity
integral1 = []

for i in range(len(aver)):

    lower_limit= aver[i] - 5* sigma[i]

    upper_limit= aver[i] + 5* sigma[i]

    dprc = integrate_fdr(sigma, aver, i, lower_limit, upper_limit)

    integral1.append(dprc)


c = -np.array(integral1)
A_eq = np.ones((1, len(integral1)))
b_eq = np.array([1.0])

bounds = [(0.0001, None)] * len(integral1)
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
optimal_probs = result.x

channel_capacity = -result.fun

print(channel_capacity)