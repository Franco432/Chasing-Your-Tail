from pygame.mixer import Sound

# Crear clase que permitirá hacer los diálogos de las explicaciones
class dialogo():
	def __init__(self, texto, sonido, duracion = 0.03) -> None:
		self.sonido, self.cambiar, self.cowldown, self.textos, self.textos_llevados, self.ind_letra, self.ind_texto, self.momen_letra, self.max = \
		Sound(sonido), 0, duracion, texto.split('\n'), [''], 0, 0, 0, len(texto.split('\n')[0])
		self.sonido.set_volume(0.5)
	
	# Crear función que hará que cuando pase cierta cantidad de tiempo, se registre una nueva letra en su texto
	def cambiar_letra(self, time):
		if time-self.momen_letra > self.cowldown and self.ind_texto < len(self.textos):
			# Añadirse una letra a un string contenido dentro de una lista que se muestra en el juego
			self.textos_llevados[self.ind_texto] += self.textos[self.ind_texto][self.ind_letra]
			# Actualizar índices para poder poner más letras
			self.momen_letra = time; self.ind_letra += 1
			# Ejecutar sonido algunas veces
			if not self.ind_letra%3: self.sonido.play()
			# Pasar de línea si ya terminó la linea de texto actual
			if self.ind_letra == self.max:
				# Actualizar índices para poner más textos si es que todavía quedan
				self.ind_texto += 1
				if self.ind_texto < len(self.textos):
					self.max = len(self.textos[self.ind_texto])
					self.ind_letra = 0
					self.textos_llevados.append('')

	# Crear función para mostrar el texto que lleva
	def mostrar_texto(self, x, y, color, font, screen):
		for num, texto in enumerate(self.textos_llevados):
			screen.blit(font.render(texto, 0, color), (x, y+num*51))
