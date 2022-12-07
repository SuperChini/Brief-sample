library(AER)             # Para el compendio de datos del libro de Kleiber & Zeileis (2008)
library(scales)          # Para las transparencias de los elementos de color.
library(quantreg)        # Para usar las regresiones por cuantiles

data("CPS1985", package = "AER") # Carga los datos del paquete AER
cps <- CPS1985           # Renombra la variable como cps
cps_lm <- lm(log(wage) ~ experience + I(experience^2) + education, data = cps) # Hace la regresión simple
cps_rq <- rq(log(wage) ~ experience + I(experience^2) + education, data = cps, tau = seq(0.2, 0.8, by = 0.15)) # Regresión por cuantiles
cps2 <- data.frame(education = mean(cps$education), experience = min(cps$experience):max(cps$experience))      # Crea un "data frame" con los datos pertinentes
cps2 <- cbind(cps2, predict(cps_lm, newdata = cps2, interval = "prediction"))  # Se agregan los valores requeridos al "data frame" anterior
cps2 <- cbind(cps2, predict(cps_rq, newdata = cps2, type = ""))                # Se agregan los valores "tau" a cps2. Los valores de los cuantiles
jpeg("salarios.jpeg", width = 924 , height=924) # Crea una imagen en el directorio actual con 924x924 px de cada lado
# Se hace la gráfica con:
plot(log(wage) ~ experience, data = cps,   # Crea el mapeo principal de datos en el gráfico
     pch=20, col="#234DEA", cex=2,    # Se crean los puntos azules rellenos
     axes=F,                          # se eliminan los ejes
     ylab= "", xlab= "")              # Se eliminan los nombres de los ejes
box(lty=2, col="#424242", lwd=2)           # Agregada una caja gris punteada
# Sigue agregar el eje de las abscisas (de las x) y el de las ordenadas
axis(1, col="#610B21", lwd=3, col.axis="#610B21", cex=2)
axis(2, col="#610B21", lwd=3, col.axis="#610B21", las=2) 
# Se agregan las leyendas a los ejes
mtext("Experiencia", side=1, cex=1.7, col="#610B21", line=2)
mtext("Logaritmo del salario", side=2, cex=1.7, col="#610B21", line=2)
for(i in 6:10) lines(cps2[,i] ~ experience, data = cps2,          # hace el mapeo de las líneas predeterminadas
                     col=alpha("#FFFF00", .75), lwd=5)           #líneas amarillas gruesas con un 75% de transperencia
title("Estimación de los salarios en forma semi-logarítmica", cex.main=2.7, col.main="#2E2E2E", 
      sub="Con base en el libro de Kleiber & Zeileis (2008) y con datos de Brendt (1991)", col.sub="#FF0000", font.sub=4, cex.sub=1.3)
# Se crearon el título y subtítulo con los colores y tipo de texto correspondientes
dev.off()           # Se cierra el archivo de imégen, JPEG en este caso
library(AER)             # Para el compendio de datos del libro de Kleiber & Zeileis (2008)
library(scales)          # Para las transparencias de los elementos de color.
library(quantreg)        # Para usar las regresiones por cuantiles

data("CPS1985", package = "AER") # Carga los datos del paquete AER
cps <- CPS1985           # Renombra la variable como cps
cps_lm <- lm(log(wage) ~ experience + I(experience^2) + education, data = cps) # Hace la regresión simple
cps_rq <- rq(log(wage) ~ experience + I(experience^2) + education, data = cps, tau = seq(0.2, 0.8, by = 0.15)) # Regresión por cuantiles
cps2 <- data.frame(education = mean(cps$education), experience = min(cps$experience):max(cps$experience))      # Crea un "data frame" con los datos pertinentes
cps2 <- cbind(cps2, predict(cps_lm, newdata = cps2, interval = "prediction"))  # Se agregan los valores requeridos al "data frame" anterior
cps2 <- cbind(cps2, predict(cps_rq, newdata = cps2, type = ""))                # Se agregan los valores "tau" a cps2. Los valores de los cuantiles
jpeg("salarios.jpeg", width = 924 , height=924) # Crea una imagen en el directorio actual con 924x924 px de cada lado
# Se hace la gráfica con:
plot(log(wage) ~ experience, data = cps,   # Crea el mapeo principal de datos en el gráfico
     pch=20, col="#234DEA", cex=2,    # Se crean los puntos azules rellenos
     axes=F,                          # se eliminan los ejes
     ylab= "", xlab= "")              # Se eliminan los nombres de los ejes
box(lty=2, col="#424242", lwd=2)           # Agregada una caja gris punteada
# Sigue agregar el eje de las abscisas (de las x) y el de las ordenadas
axis(1, col="#610B21", lwd=3, col.axis="#610B21", cex=2)
axis(2, col="#610B21", lwd=3, col.axis="#610B21", las=2) 
# Se agregan las leyendas a los ejes
mtext("Experiencia", side=1, cex=1.7, col="#610B21", line=2)
mtext("Logaritmo del salario", side=2, cex=1.7, col="#610B21", line=2)
for(i in 6:10) lines(cps2[,i] ~ experience, data = cps2,          # hace el mapeo de las líneas predeterminadas
                     col=alpha("#FFFF00", .75), lwd=5)           #líneas amarillas gruesas con un 75% de transperencia
title("Estimación de los salarios en forma semi-logarítmica", cex.main=2.7, col.main="#2E2E2E", 
      sub="Con base en el libro de Kleiber & Zeileis (2008) y con datos de Brendt (1991)", col.sub="#FF0000", font.sub=4, cex.sub=1.3)
# Se crearon el título y subtítulo con los colores y tipo de texto correspondientes
# Se cierra el archivo de imégen, JPEG en este caso
require(maps) # activación de librería
require(mapproj) # se usará para projection="polyconic"
# Cargar los datos
# unemp incluye datos para condados de los Estados Unidos continentales. Se excluyen Alaska, Hawaii, Puerto Rico, y pequeñas ciudades de Virginia
data(unemp) # Datos de desempleo
data(county.fips) # mapa de los condados

# Se define la paleta de colores. Escala de grises en este caso. En el original, rosas y magenta.
colors = c("#F1EEF6", "#D3D3D3", "#B9B9B9", "#787878", "#2E2E2E", "#111111") # Colores
unemp$colorBuckets <- as.numeric(cut(unemp$unemp, c(0, 2, 4, 6, 8, 10, 100))) # Rangos de desempleo
leg.txt <- c("<2%", "2-4%", "4-6%", "6-8%", "8-10%", ">10%") # Etiquetas de los rangos

# Se alinean los datos con definiciones de mapa (parciales) de emparejamientos de estados, 
#         nombre de condados, que incluyen varios polígonos para algunos condados
cnty.fips <- county.fips$fips[match(map("county", plot=FALSE)$names, county.fips$polyname)]
colorsmatched <- unemp$colorBuckets [match(cnty.fips, unemp$fips)]

# Se dibuja el mapa. Luego se guarda en JPEG.
jpeg("desempleo Estados Unidos 2009.jpg", width = 1024, height=750) # Crea imagen de 1024 x 750 pixeles.
map("county", col = colors[colorsmatched], fill = TRUE, resolution = 0, lty = 0, projection = "polyconic") # Mapa general del desempleo en grises
map("state", col = "white", fill = FALSE, add = TRUE, lty = 1, lwd = 0.2, projection="polyconic") # Mapa de los estados sobre puesto
title(main="Desempleo por condado, año 2009", cex.main = 3,
      sub="Creado con información de la solución de J del 'Choropleth Challenge' 
           más info en http://blog.revolutionanalytics.com/2009/11/choropleth-challenge-result.html")
# Se creó el título del mapa
legend("top", leg.txt, horiz = T, fill = colors, bg="#F1F1F1", cex=1.5) # Indicación de los colores por su rango
map.axes() # Para colocar ejes con la latitud y longitud
dev.off()
# Para ver los límites del condado débiles, vaya a RGui : File/SaveAs/PDF
