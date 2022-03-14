import numpy as np
import numericoii2021 as nu2

n = 50
A, b = nu2.matrizCalor(n) # genera matriz usando scipy.sparse.csr_matrix
print('dim(A) = ', A.shape)
print(A)

print("Cholesky")
%time xChol = nu2.sol_defpos(A,b)

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

h = 1/(n-1)
grilla = h*np.arange(1,n-1)
X, Y = np.meshgrid(grilla, grilla)

fig, ax = plt.subplots(1,2,subplot_kw={'projection':'3d'},figsize=[12.8,4.8])
ax[0].plot_surface(X,Y,b.reshape((n-2,n-2)))
ax[0].set_title('fuente de calor')
U = xChol.reshape((n-2,n-2))
ax[1].plot_surface(X,Y,U)
ax[1].set_title(f'temperatura final, residuo = {np.linalg.norm(b-A.dot(xChol))}');

print("## Cauchy ##")
%time xCauchy = nu2.sol_cauchy(A,b,np.zeros_like(b), maxiter=10000)

fig, ax = plt.subplots(1,2,subplot_kw={'projection':'3d'},figsize=[12.8,4.8])
ax[0].plot_surface(X,Y,b.reshape((n-2,n-2)))
ax[0].set_title('fuente de calor')
U = xCauchy.reshape((n-2,n-2))
ax[1].plot_surface(X,Y,U)
ax[1].set_title(f'temperatura final, residuo = {np.linalg.norm(b-A.dot(xCauchy))}');