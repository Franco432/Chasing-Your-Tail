from sources.imagen import imagen
from pygame.mixer import Sound

# Definir clase de botón
class buton(imagen):
	def __init__(self, sprite, x, y, w, h, sonido_posar, sonido_presionar) -> None:
		super().__init__(sprite, x, y, w, h)
		self.presionado = 0
		self.sonidos = (Sound(sonido_posar), Sound(sonido_presionar))
		for sonido in self.sonidos: sonido.set_volume(0.25)

	# Crear función para cambiar de color cuando el mouse está o no encima de él
	def cambiar_color(self, pos_mouse):
		# Si el mouse está sobre él y aún no se ha dado cuenta
		if self.rect.collidepoint(pos_mouse):
			if not self.presionado:
				# Ponerse como "presionado"
				self.presionado = True
				# Cambiar su imagen a un botón apretado
				self.cambiar_imagen(self.sprite[:-4]+'_rojo'+self.sprite[-4:], self.x, self.y, self.w, self.h)
				self.sonidos[0].stop()
				self.sonidos[0].play()

		# Si el mouse no está sobre él, pero él cree que sí
		elif self.presionado:
			# Dejar de estar como "presionado"
			self.presionado = False
			# Cambiar su imagen a un botón sin apretar
			self.cambiar_imagen(self.sprite[:-9]+self.sprite[-4:], self.x, self.y, self.w, self.h)
