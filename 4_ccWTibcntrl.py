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
r1j1 = np.array([19233, 19939, 18577, 10164, 1434, 338, 270, 284, 284])
r1j2 = np.array([19979, 20608, 19071, 10538, 1446, 340, 268, 290, 272])
r1j3 = np.array([15681, 17203, 17505, 7070, 1260, 466, 386, 412, 370])
r1j4 = np.array([15759, 18277, 17325, 7572, 1230, 436, 372, 370, 306])
r1j5 = np.array([15555, 16283, 16653, 15989, 8910, 750, 218, 174, 184])
r1j6 = np.array([15697, 16071, 16137, 15391, 8486, 762, 200, 192, 162])

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