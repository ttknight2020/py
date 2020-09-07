def incsearch(func, xmin, xmax, ns=50):
    '''
    incsearch: incremental search root locator
        xb = incsearch(func, xmin, xmax, ns):
            finds brackets of x that contain sign changes
            of a function on an interval 
    input:
        func = name of function 
        xmin, xmax = endpoints of interval 
        ns = number of subintervals 
    output:
        xb[k-1][0] is the lower bound of the kth sign change 
        xb[k-1][1] is the upper bound of the kth sign change 
        if no brackets found, xb = []
    '''
    import numpy as np 
    x = np.linspace(xmin, xmax, ns)
    f = func(x)
    nb = 0
    xb = []
    for k in range(len(x)):
        if f(x[k]) * f(x[k+1]) <= 0:
            nb += 1
            xb[nb-1][0] = x[k]
            xb[nb-1][1] = x[k+1]
    if nb:
        print('no brackets found')
        print('check interval or increase ns')
    else:
        print('number of brackets:')
        print(nb)
    