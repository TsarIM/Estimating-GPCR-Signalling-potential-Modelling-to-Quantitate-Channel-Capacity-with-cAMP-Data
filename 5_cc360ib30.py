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
r1j1 = np.array([20308, 22538, 23654, 21890, 11516, 966, 286, 260, 218])
r1j2 = np.array([19119, 21614, 22858, 20760, 12652, 950, 280, 254, 230])
r1j3 = np.array([22944, 24404, 24322, 10452, 1646, 618, 564, 520, 514])
r1j4 = np.array([20516, 23984, 22470, 9440, 1462, 548, 488, 472, 418])
r1j5 = np.array([23330, 24010, 23492, 13544, 1898, 466, 388, 370, 358])
r1j6 = np.array([23870, 24759, 24551, 13584, 1828, 450, 348, 350, 342])

# conc= np.array([-6, -7, -8, -9, -10, -11, -12, -13, -14])

log10r1j1=np.log10(r1j1)

log10r1j2=np.log10(r1j2)

log10r1j3=np.log10(r1j3)

log10r1j4=np.log10(r1j4)

log10r1j5=np.log10(r1j5)

log10r1j6=np.log10(r1j6)

aver=(log10r1j1+log10r1j2+log10r1j3+log10r1j4+log10r1j5+log10r1j6)/nr

sigma = np.std([log10r1j1,log10r1j2,log10r1j3,log10r1j4,log10r1j5,log10r1j6],axis=0)

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