import matplotlib.pyplot as plt
import numpy as np

A = np.array([[3., 6], [1, 2]])
print('A=')
print(A)

fig, ax = plt.subplots(1,1)
theta = np.linspace(0, 2*np.pi, 300)
# norma 2
esfera2 = np.array([np.cos(theta), np.sin(theta)]) # esfera unidad
imgesfera2 = A @ esfera2  # mapeo de la esfera unidad
ax.plot(esfera2[0], esfera2[1], color='b', label='$S_2$')
ax.plot(imgesfera2[0], imgesfera2[1], color='c', label='$A S_2$' )

# norma infinito
r = 1/np.maximum(np.abs(esfera2[0]), np.abs(esfera2[1]))
esferainf = np.array([r*esfera2[0], r*esfera2[1]]) # esfera unidad
imgesferainf = A @ esferainf # mapeo de la esfera unidad
ax.plot(esferainf[0], esferainf[1], color='r', label='$S_\infty$')
ax.plot(imgesferainf[0], imgesferainf[1], color='m', label='$A S_\infty$' )
ax.axis('equal')
ax.legend();