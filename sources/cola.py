from random import random
from sources.imagen import imagen

class cola():
	def __init__(self, ruta) -> None:
		# Crear tuplas con todos los frames de las animaciones que va a tener
		sprites = (
			(ruta+'cola_abj_a.png', 256, 540),
			(ruta+'cola_abj_d.png', 256, 540),
			(ruta+'cola_abj_f.png', 256, 540),
			(ruta+'cola_abj_h.png', 256, 540),
			(ruta+'cola_arr_a.png', 256, 540),
			(ruta+'cola_arr_d.png', 256, 540),
			(ruta+'cola_arr_f.png', 256, 540),
			(ruta+'cola_arr_h.png', 256, 540),
			(ruta+'cola_cor_a.png', 256, 540),
			(ruta+'cola_cor_d.png', 256, 540),
			(ruta+'cola_cor_f.png', 256, 540),
			(ruta+'cola_cor_h.png', 256, 540),
		)
		# Crear lista con todos los frames de sus animaciones
		self.imagenes = [imagen(sprite[0], 0, 0, sprite[1], sprite[2]).image for sprite in sprites]
		# Guardar su imagen actual como la superficie de su primer frame
		self.image = self.imagenes[0]
		# Definir su pocición en pantalla
		self.pos = [0, 50]
		# Definir el último momento en que cambio la pocisión de la cola y de pata
		self.camCola = self.camPata = 0
		# Definir el cowldown para cambiar de pata y de cola
		self.cowldown_pata = self.cowldown_cola = 0
		# Definir el estado de su cola
		self.cola = 0
		# Crear variable que dirá qué pata está moviendo
		self.pata = 0
		# Crear variable que dirá cuál es la dirección en la que está yendo
		self.derecha = -1
		# Crear diccionario que vincula sus patas
		self.dic = {0:3, 3:0, 1:2, 2:1}

	# Definir función que cambie la animación de la cola
	def cambiar(self, vel_fondo, time):
		# Si el fondo cambió de dirección
		if self.derecha != (vel_fondo > 0):
			self.derecha = (vel_fondo > 0)
			# Definir con la cola si está corriendo o caminando
			self.cola = 0 if abs(vel_fondo) < 100 else 2
			# Definir su cowldown de cambio de pata según si está o no corriendo
			self.cowldown_pata = 0.325 if self.cola == 2 else 0.75
			# Cambiar su pocisión en la pantalla según si está yendo hacia la derecha o caminando
			self.pos[0] = 0 if self.derecha else 1024
			# Cambiar su imagen y sus teclas de acuerdo a su dirección
			if self.derecha:
				self.pata = 0
				# Cambiar su imagen
				self.image = self.imagenes[0+self.cola*4]
			else:
				self.pata = 2
				# Cambiar su imagen
				self.image = self.imagenes[2+self.cola*4]

		# Si debe mover una pata
		if time-self.camPata > self.cowldown_pata:
			# Hacer y guardar el cambio
			self.pata = self.dic[self.pata]
			self.camPata = time
			# Cambiar su imagen
			self.image = self.imagenes[self.pata+self.cola*4]

		# Si debe mover la cola
		if time-self.camCola > self.cowldown_cola and self.cola != 2:
			# Guardar el cambio
			self.camCola = time
			self.cowldown_cola = 0.5+random()
			self.cola = not self.cola
			# Cambiar su imagen
			self.image = self.imagenes[self.pata+self.cola*4]
