# DISTRIBUCIÓN NORMAL (TIPIFICACIÓN)
x = seq(from=-4, to=4, by=0.01) # recorremos eje x
y = dnorm(x=x) # calculamos las f(x)
plot(x, y, type="l", main="Campana de Gauss", 
     xlab="x", ylab="Densidad de la normal", 
     col="red", lwd=3)
points(x=c(-4,4), y=c(0,0), type="l") # dibujamos eje X con 2 puntos
# vamos a lanzar 1000 puntos al azar en el recuadro
xx = runif(n=1000, min=-4, max=4) # sus coordenadas X
yy = runif(n=1000, min=0, max=1) # sus coordenadas Y
points(xx, yy) # los pintamos como puntos
dentro = yy < dnorm(xx) # condición "estar dentro de la gráfica"
color= rep("green", 1000) # vector de colores constante
color[dentro] = "red" # cambio a rojo si están dentro
points(xx, yy, col=color) # pinto de nuevo con color