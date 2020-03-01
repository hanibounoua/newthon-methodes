## let's set a function f and let dx been its derrivative


def Newton_root_methode(x_0, fun, dx, threshold):
    y = []
    dydx = []
    x = []
    x.append(x_0)
    y.append(fun(x[0]))
    dydx.append(dx(x[0]))
    i = 1
    while True:
        x.append(x[i-1] - y[i-1]/dydx[i-1])
        y.append(fun(x[i]))
        dydx.append(dx(x[i]))
        if abs(y[i]) <= threshold:
            break
        else:
            i += 1
    return {"x": x, "Function Values": y, "First derrivative repect to x values": dydx}
