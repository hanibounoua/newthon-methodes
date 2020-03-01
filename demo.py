from Root_finding_methods import Newton_root_methode

def f(x):
    return  x**2 + x - 2
def df(x):
    return 2*x + 1
print(Newton_root_methode(0, f, df, .001))
