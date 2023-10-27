# Crear función de pantalla de carga, que se ejecutará en un hilo separado al que crea las clases
def pantalla_carga(juego):
	# Importaciones del funcionamiento de la pantalla de carga
	from math import sin, cos
	from pygame.draw import circle
	from pygame.display import update
	# Crear variable para hacer que los circulos roten
	num = 0
	# Crear bucle para la pantalla de carga
	while juego['cargando']:
		# Actualizar las pocisiones de los circulitos
		num += 0.01
		try:
			# Llenar la pantalla de verde
			juego['screen'].fill((50, 100, 25))
			# Dibujar los circulitos
			for x in (0, 1.5, 3, 4.5): circle(juego['screen'], (230, 230, 200), (640+sin(num+x)*30, 360-cos(num+x)*30), 10)
			# Actualizar la pantalla
			update()
		except: juego['cargando'] = juego['ejecutando'] = False
