
import numpy as np

def autjacobi2D(A):
    '''
    c, s = autjacobi2D(A) diagonaliza A 2x2 simétrica,
    encuentra Q=[[c, -s], [s, c]] t.q. D = Q.T A Q
    Método de Jacobi.
    '''
    if A[0, 1] != 0:
        tau = (A[1, 1] - A[0, 0]) / (2 * A[0, 1])
        if tau >= 0:
            t = -1 / (tau + np.sqrt(tau ** 2 + 1))
        else:
            t = 1 / (-tau + np.sqrt(tau ** 2 + 1))

        c = 1 / np.sqrt(1 + t ** 2)
        s = t * c
    else:
        c = 1
        s = 0

    return c, s

A = np.random.randn(2,2)
A = 0.5*(A + A.T)
print("A=")
print(A)
c, s = autjacobi2D(A)
Q = np.array([[c, -s], [s, c]])
print("\nmétodo de Jacobi")
print('Q.T @ A @ Q=')
print(Q.T @ A @ Q)
npeig = np.linalg.eigvals(A)
print("\nusando numpy")
print(f'autovalores={npeig}')

