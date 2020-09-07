def newtraph(func, dfunc, xr, es=0.00001, maxit, *varargin):
    '''
    newtraph: Newton-Raphson root location zeros
    [root, ea, iter] = newtraph(func, dfunc, xr, es, maxit, p1, p2,...):
        uses Newton-Raphson method to find the root of func 
    input:
        func = name of function 
        dfunc = name of derivative of function 
        xr = initial guesses 
        es = desired relative error (default=0.0001%)
        maxit = maximum allowable iterations (default=50)
        p1, p2, ... = additional parameters used by function 
    output:
        root = real root
        ea = approximate relative error (%)
        iter = number of iterations
    '''
    iter = 0
    while True:
        xrold = xr
        xr = xr - func(xr) / dfunc(xr)
        iter = iter + 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100 
        if ea <= es or iter >=maxit:
            break 
    root = xr 
    return root, ea, iter 
    


