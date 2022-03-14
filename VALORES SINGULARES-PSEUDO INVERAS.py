import numpy as np
import matplotlib.pyplot as plt

#A = np.array([[5,1], [1,-2]])
A = np.round(100*np.random.randn(2,2))
U, S, Vt = np.linalg.svd(A)
print('A=')
print(A)
print('U=')
print(U)
print('S=')
print(S)
print('¡OJO! la SVD de numpy retorna V.T en vez de V')
print('V.T=')
print(Vt)
print('USV.T=')
print(U@ np.diag(S) @ Vt)


