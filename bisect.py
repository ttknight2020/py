def bisect(func, xl, xu, es=0.0001, maxit=50, *varargin):
    '''
    bisect:root location zeros
    [root, ea, iter] = bisect(func, xl, xu, es, maxit, p1, p2, ...):
        uses bisection method to find the root of func 
    input:
        func = name of function 
        xl, xu = lower and upper guesses
        es = desired relative error(default = 0.0001%)
        maxit = maximum allowable iterations (default = 50)
        p1, p2,... = additional parameters used by func 
    output:
        root = real root
        ea = approximate relative error (%)
        iter = number of iterations
    '''

    test = func(xl, varargin) * func(xu, varargin)
    if test > 0:
        print('no sign change')
        return 'null' , 'null', 'null'
    iter = 0
    xr = xl 

    while True:
        xrold = xr
        xr = (xl + xr) /2 
        iter += 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        test = func(xl, varargin) * func(xu, varargin)

        if test < 0:
            xu = xr 
        elif test > 0:
            xl = xr 
        else:
            ea = 0
        if ea <= es or iter >= maxit:
            break 

    root = xr 
    return root, ea, iter 


