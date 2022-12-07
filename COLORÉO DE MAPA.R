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

