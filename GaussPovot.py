def GaussPivot(A, b):
    '''
    GaussPovot: Gauss elimination povoting 
    x = GaussPivot(A, b): Gauss elimination with pivoting.
    input:
        A = coefficient matrix 
        b = right hand side vector 
    output:
        x = solution vector 
    '''
    import numpy as np
    m, n = A.shape
    if m != n:
        print('Matrix A must be square')
    
    
