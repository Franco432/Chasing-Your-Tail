from sources.imagen import imagen
from random import randint, random

class fondo():
	def __init__(self, ruta) -> None:
		# Crearse dos imágenes, pues se irán moviendo para aparentar que cambiamos de pocisión
		self.fondo1 = imagen(ruta+'fondo_1.jpg', 0, 0, 1280, 720)
		self.fondo2 = imagen(ruta+'fondo_2.jpg', 1280, 0, 1280, 720)
		# Crear variable que dirá hacia qué dirección moverse
		self.velocidad = random()*2-1
		# Crear variable para saber cuándo fue la última vez que cambió de dirección y su cowldown
		self.cambio = self.cowldown = 0
	
	# Definir función para mover el fondo y cambiar su velocidad
	def moverse(self, dt, time):
		# Mover ambos fondos a la velocidad que debe
		self.fondo1.x += dt*self.velocidad*30
		self.fondo2.x += dt*self.velocidad*30
		
		# Cambiar el lugar de los fondos si salieron totalmente de la pantalla
		if self.fondo1.x >= 1280: self.fondo1.x = 0; self.fondo2.x = 1280
		elif self.fondo2.x >= 1280: self.fondo2.x = 0; self.fondo1.x = 1280
		elif self.fondo1.x <= -1280: self.fondo1.x = 1280; self.fondo2.x = 0
		elif self.fondo2.x <= -1280: self.fondo2.x = 1280; self.fondo1.x = 0

		# Si ya pasó el momento de cambiar de velocidad, cambiarla
		if time-self.cambio > self.cowldown:
			# Cambiar sus referencias de tiempo
			self.cambio = time
			self.cowldown = randint(3, 10)
			# Cambiar su velocidad
			self.velocidad = random()*40-20

