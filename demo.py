from Newton_s_Algorithms import Newton_root_Algorithm, Newton_optimization_algrithm

def f(x):
    return  x**2 + x - 2
def df(x):
    return 2*x + 1
def ddf(x):
    return 2
print(Newton_root_Algorithm(0, f, df, .001))
print(Newton_optimization_algrithm(0, f, df, ddf, .1, .0001))
