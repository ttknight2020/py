def GaussNaive(A, b):
    '''
    GaussNaive: naive Gauss elimination
        x = GaussNaive(A, b): Gauss elimination without pivoting 
    input:
        A = coefficient matrix 
        b = right hand side vector
    output:
        x = soultion vector 
    '''
    import numpy as np 
    m, n = A.shape
    if m != n:
        print('Matrix A must be square')
    
    Aug = np.hstack((A, b[:, np.newaxis]))   #矩阵下标有问题
    for k in range(n-1):
        for i in range(k + 1, n):
            factor = Aug[i, k] / Aug[k, k]
            Aug[i,k:n] = Aug[i, k:n] - factor*Aug[k, k:n]
    
    X = np.zeros(n)
    X[n-1] = Aug[n-2, n-1] / Aug[n-2, n-2]
    for i in range(n-2, -1, -1):
        X[i] = (Aug[i, n] - Aug[i, i+1:n-1] * X[i+1:n-1]) / Aug[i, i]
    return X 

if __name__ == '__main__':
    import numpy as np
    A = np.array([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]])
    b = np.array([7.85, -19.3, 71.4])
    X = GaussNaive(A, b)
    print(X) 
            