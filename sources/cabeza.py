from sources.imagen import imagen

class cabeza():
	def __init__(self, ruta) -> None:
		# Crear tuplas con todos los frames de las animaciones que va a tener
		sprites = (
			(ruta+'cabeza.png', 256, 540),
		)
		# Crear lista con todos los frames de sus animaciones
		self.imagenes = [imagen(sprite[0], 0, 0, sprite[1], sprite[2]) for sprite in sprites]
		# Guardar su imagen actual como la superficie de su primer frame
		self.imagen = self.imagenes[0]
		self.image = self.imagen.image
		# Definir su pocición en pantalla
		self.pos = (1280-self.imagen.w*3/4, 720-self.imagen.h*3/4)

