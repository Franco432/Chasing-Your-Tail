from sources.escenas import *
from sources.cabeza import cabeza
from sources.cola import cola
from sources.fondo import fondo

# Definir el juego
class juego():
	def __init__(self, juego) -> None:
		self.juego = juego
		# Crear las partes del perro
		self.cabeza = cabeza(path_juego+'images/perro/')
		self.cola = cola(path_juego+'images/perro/')
		# Añadir el fondo para que lo dibuje
		self.fondo = fondo(path_juego+'images/')
		# Añadir botón de pausa
		self.boton_pausa = buton(path_juego+'images/pause.png', 1150, 10, 100, 60, path_juego+'sounds/sonido_posarse.ogg', path_juego+'sounds/sonido_presionar.ogg')

	# Controlar lo que pasa en la partida
	def funciones(self):
		# Obtener la pocisión del mouse
		self.pos_mouse = get_pos()
		# Obtener el momento del frame
		self.time = get_ticks()/1000
		# Controlar los botones
		Thread(target=self.boton_pausa.cambiar_color, args=(self.pos_mouse,)).start()
		# Controlar al perro
		self.perro()
		# Obtener y reaccionar a los eventos del usuario
		self.eventos()
		# Dibujar cosas en pantalla
		self.dibujar()
	
	# Crear función para dibujar en la pantalla
	def dibujar(self):
		# Crear variable de la pantalla para no tener que estar copiando algo tan largo
		screen = self.juego['screen']
		# Borrar la pantalla
		screen.fill((0, 0, 0))
		# Dibujar el fondo, que está separado en dos imágenes
		screen.blit(self.fondo.fondo1.image, (self.fondo.fondo1.x, 0))
		screen.blit(self.fondo.fondo2.image, (self.fondo.fondo2.x, 0))
		# Mostrar las partes del perro
		screen.blit(self.cola.image, self.cola.pos)
		screen.blit(self.cabeza.image, self.cabeza.pos)
		# Dibujar su botón en pantalla
		screen.blit(self.boton_pausa.image, (self.boton_pausa.x, self.boton_pausa.y))
		
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

	# Definir función para controlar al perro
	def perro(self):
		Thread(target=self.fondo.moverse, args=(self.juego['dt'], self.time)).start()
