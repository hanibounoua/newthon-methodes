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

def W_Newton_root_Algorithm(x_0, fun, dx, threshold , lr=1,max_ittr=1000):
    y = fun(x_0)
    dydx = dx(x_0)
    x = x_0
    i = 0
    while abs(y)>threshold:
        x=(x - lr * y/dydx)
        y=(fun(x))
        dydx=(dx(x))
        i += 1
        if i > max_ittr:
            print("couldn't converge")
            break
    return x

def W_Newton_optimization_algrithm(x_0, fun, dfdx, ddfddx, learningRate, threshold):
    xm=W_Newton_root_Algorithm(x_0,dfdx,ddfddx,threshold,learningRate)
    if ddfddx(xm)>threshold:
        x_type='minima'
    elif ddfddx(xm)<-threshold:
        x_type='maxima'
    else:
        x_type='saddle'
    return {"x":xm,"f(x)":fun(xm),"point_type":x_type}
