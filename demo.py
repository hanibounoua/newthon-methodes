from Newton_s_Algorithms import W_Newton_optimization_algrithm,W_Newton_root_Algorithm

def f(x):
    return  x**2 + x - 2
def df(x):
    return 2*x + 1
def ddf(x):
    return 2

print("solution for f(x)=0 is:")
print(W_Newton_root_Algorithm(0, f, df, .001))


print("optimisation of f(x)")
print(W_Newton_optimization_algrithm(0, f, df, ddf, .1, .0001))
