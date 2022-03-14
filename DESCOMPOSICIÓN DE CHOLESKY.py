# construimos la matriz anterior
import numpy as np
n = 50 # cantidad de nodos interiores
E = np.diag(np.ones(n-1), 1) + np.diag(np.ones(n-1), -1)
I = np.eye(n)
print('\n')
print('A')
A = np.kron(I, 4*I - E) + np.kron(E, -I)
print(A)
print('\n')
print('dimensión de A :', A.shape)
print('\n')
# construimos el término no homogéneo
h = 1/(n+1)
grilla = h*np.arange(1,n+1)
print('nodos interiores =',grilla)
print('\n')
X, Y = np.meshgrid(grilla, grilla)
f = 10*(np.sqrt((X-0.5)**2 + (Y-0.5)**2) <= 0.1)
print('fuente de calor')
print('\n')
print(f)
b = h**2*f.reshape(n**2)
print('\n')