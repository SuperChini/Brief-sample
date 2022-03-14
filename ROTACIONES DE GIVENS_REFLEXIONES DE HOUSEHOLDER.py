import numpy as np

def house(x):
    '''
    u, rho = house(x)
    Calcula u y rho tal que Q = I - rho u u^T
    cumple Qx = \|x\|_2 e^1
    '''
    n = len(x)
    rho = 0
    u = x.copy()
    u[0] = 1.

    if n == 1:
        sigma = 0
    else:
        sigma = np.sum(x[1:] ** 2)

    if sigma > 0 or x[0] < 0:
        mu = np.sqrt(x[0] ** 2 + sigma)
        if x[0] <= 0:
            gamma = x[0] - mu
        else:
            gamma = -sigma / (x[0] + mu)

        rho = 2 * gamma ** 2 / (gamma ** 2 + sigma)
        u = u / gamma
        u[0] = 1

    return u, rho

m, n = 5, 3
A = np.random.randint(10, size=(m,n))
print('matriz A original')
print(A)
print('\naplicamos una reflexión en la primera columna')
u, rho = house(A[:,0])
A = A - np.outer(rho*u, u.T @ A)
print(A)
print('\naplicamos una reflexión en la segunda columna')
u, rho = house(A[1:,1])
A[1:, 1:] = A[1:, 1:] - np.outer(rho*u, u.T @ A[1:, 1:])
print(A)
