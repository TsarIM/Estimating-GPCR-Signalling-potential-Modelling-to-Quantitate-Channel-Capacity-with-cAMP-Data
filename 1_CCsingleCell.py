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

nr=3
r1j1 = np.array([0.872,0.851, 0.894, 0.934, 1.081, 1.113])
r1j2 = np.array([0.758,0.755, 0.793, 0.914, 1.045, 1.212])
r1j3 = np.array([0.795,0.811, 0.821, 0.968, 1.11, 1.235])


log10r1j1=np.log10(r1j1)

log10r1j2=np.log10(r1j2)

log10r1j3=np.log(r1j3)


aver=(log10r1j1+log10r1j2+log10r1j3)/nr

sigma = np.std([log10r1j1,log10r1j2,log10r1j3], axis=0)

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
