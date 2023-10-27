from sources.escenas import *

# Definir el juego
class juego():
	def __init__(self, juego) -> None:
		self.juego = juego
		# Crear grupo que contendrá sus imágenes
		self.grupo = Group()
		# Añadir el fondo para que lo dibuje
		self.grupo.add(imagen(path_juego+'images/fondo.jpg', 0, 0, 1280, 720))
		# Añadir botón de pausa
		self.boton_pausa = buton(path_juego+'images/pause.png', 1150, 10, 100, 60, path_juego+'sounds/sonido_posarse.ogg', path_juego+'sounds/sonido_presionar.ogg')
		self.grupo.add(self.boton_pausa)

	# Controlar lo que pasa en la partida
	def funciones(self):
		# Obtener la pocisión del mouse
		self.pos_mouse = get_pos()
		# Controlar los botones
		Thread(target=self.boton_pausa.cambiar_color, args=(self.pos_mouse,)).start()
		# Obtener y reaccionar a los eventos del usuario
		self.eventos()
		# Dibujar cosas en pantalla
		self.dibujar()
	
	# Crear función para dibujar en la pantalla
	def dibujar(self):
		# Borrar la pantalla
		self.juego['screen'].fill((0, 0, 0))
		# Dibujar los sprites en pantalla
		self.grupo.draw(self.juego['screen'])
		# Actualizar la pantalla
		flip()
	
	# Definir función para recibir inputs del usuario
	def eventos(self):
		for event in get():
			# Salir del juego
			if event.type == QUIT: self.juego['ejecutando'] = False
			# Si presionó el mouse con click izquierdo
			if event.type == MOUSEBUTTONUP and event.button == 1:
				# Poner la pausa si apretó el botón de pausa
				if self.boton_pausa.presionado:
					self.juego['escena_actual'] = 'pausa'
					# Poner sonido del botón
					Thread(target=self.boton_pausa.sonidos[1].play).start()
					# Poner música de la cueva cuando se juega la partida
					Thread(target=musicar, args=(path_pausa+'music/musica_pausa.ogg',1.5)).start()
