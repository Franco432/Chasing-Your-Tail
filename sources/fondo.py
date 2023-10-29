from sources.imagen import imagen
from random import random

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
		self.fondo1.x += dt*self.velocidad
		self.fondo2.x += dt*self.velocidad
		
		# Cambiar el lugar de los fondos si salieron totalmente de la pantalla
		if self.fondo1.x >= 1280: self.fondo1.x = -1279; self.fondo2.x = -1
		elif self.fondo2.x >= 1280: self.fondo2.x = -1279; self.fondo1.x = -1
		elif self.fondo1.x <= -1280: self.fondo1.x = 1279; self.fondo2.x = 1
		elif self.fondo2.x <= -1280: self.fondo2.x = 1279; self.fondo1.x = 1

		# Si ya pasó el momento de cambiar de velocidad, cambiarla
		if time-self.cambio > self.cowldown:
			# Cambiar sus referencias de tiempo
			self.cambio = time
			self.cowldown = 1+random()*4
			# Cambiar su velocidad
			# Crear una velocidad aleatoria
			velocidad = random()*300-150
			# Hacer que su velocidad solo pueda estar en dos rangos separados para que sea fácil para el jugador saber qué tan rápido moverse
			if velocidad > 0:
				self.velocidad = velocidad if velocidad > +100 or velocidad < +50 else (+101 if velocidad > +100 else +49)
			else:
				self.velocidad = velocidad if velocidad < -100 or velocidad > -50 else (-101 if velocidad < -100 else -49)
