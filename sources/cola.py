from sources.imagen import imagen

class cola(imagen):
	def __init__(self, ruta) -> None:
		# Crear tuplas con todos los frames de las animaciones que va a tener
		sprites = (
			(ruta+'cola.png', 256, 650),
		)
		# Crear lista con todos los frames de sus animaciones
		self.imagenes = [imagen(sprite[0], 0, 0, sprite[1], sprite[2]) for sprite in sprites]
		# Guardar su imagen actual como la superficie de su primer frame
		self.imagen = self.imagenes[0]
		self.image = self.imagen.image
		# Definir su pocición en pantalla
		self.pos = (self.imagen.w*3/4-self.imagen.w, 720-self.imagen.h*3/4)
