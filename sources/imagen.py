from pygame.sprite import Sprite
from pygame.transform import scale
from pygame import image

class imagen(Sprite):
	# Función que se ejecutará al crear la instancia de clase
	def __init__(self, sprite, x, y, w, h) -> None:
		# Configurarse cosas para poder tener una imagen
		super().__init__()
		self.cambiar_imagen(sprite, x, y, w, h)
		self.x, self.y, self.w, self.h = x, y, w, h
	# Función de cambiarse la imagen
	def cambiar_imagen(self, nueva_imagen, x, y, w, h):
		self.sprite = nueva_imagen
		self.image = image.load(self.sprite).convert()
		self.image.set_colorkey((0, 0, 0))
		self.image = scale(self.image, (w, h))
		# Obtener hitbox de su imagen
		self.rect = self.image.get_rect()
		# Pocisionar su imagen en las coordenadas en pantalla
		self.rect.x, self.rect.y = x, y
