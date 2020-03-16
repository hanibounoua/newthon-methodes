#test comment 

def Newton_root_Algorithm(x_0, fun, dx, threshold):
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


def Newton_optimization_algrithm(x_0, fun, dfdx, ddfddx, learningRate, threshold):
    y = []
    dydx = []
    ddyddx = []
    x = []
    x.append(x_0)
    y.append(fun(x[0]))
    dydx.append(dfdx(x[0]))
    ddyddx.append(ddfddx(x[0]))
    i = 1
    while True:
        x.append(x[i-1] - learningRate * dydx[i-1]/ddyddx[i-1])
        y.append(fun(x[i]))
        dydx.append(dfdx(x[i]))
        ddyddx.append(ddfddx(x[i]))
        if abs(dydx[i]) <= threshold:
            break
        else:
            i += 1
    return {"x": x, "Function Values": y, "Tangent Slope": dydx}
