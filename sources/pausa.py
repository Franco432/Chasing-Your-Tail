from sources.escenas import *

class pausa():
	def __init__(self, juego) -> None:
		self.juego = juego
		# Crear variable para guardar el momento en que se puso la pausa
		self.inicio = 0
		# Crear grupo que contendrá sus imágenes
		self.grupo = Group()
		# Añadir el fondo para que lo dibuje
		self.grupo.add(imagen(path_pausa+'images/fondo.jpg', 0, 0, 1280, 720))
		# Añadir botones
		self.botones = {'quit':buton(path_pausa+'images/exit.png'  , 460, 450, 300, 150, path_pausa+'sounds/sonido_posarse.ogg', path_pausa+'sounds/sonido_presionarse.ogg'),
						'play':buton(path_pausa+'images/resume.png', 435, 250, 350, 150, path_pausa+'sounds/sonido_posarse.ogg', path_pausa+'sounds/sonido_presionarse.ogg'),}
		# Añadir los sprites de los botones
		for boton in self.botones: self.grupo.add(self.botones[boton])
	
	# Función que ejecutará las funciones de cada frame
	def funciones(self):
		# Obtener la pocisión del mouse
		self.pos_mouse = get_pos()
		# Controlar los botones
		self.color_buttons()
		# Obtener y reaccionar a los eventos del usuario
		self.eventos()
		# Dibujar cosas en pantalla
		self.dibujar()
	
	# Definir función para recibir inputs del usuario
	def eventos(self):
		for event in get():
			# Salir del juego
			if event.type == QUIT: self.juego['ejecutando'] = False
			# Si presionó el mouse con click izquierdo
			if event.type == MOUSEBUTTONUP and event.button == 1:
				# Hacer los eventos de los botones
				Thread(target=self.eventos_buttons).start()
	
	# Crear función para dibujar en la pantalla
	def dibujar(self):
		# Borrar la pantalla
		self.juego['screen'].fill((0, 0, 0))
		# Dibujar los sprites en pantalla
		self.grupo.draw(self.juego['screen'])
		# Actualizar la pantalla
		flip()
	
	# Crear función para controlar los botones
	def color_buttons(self):
		# Actualizar el color de todos sus botones
		for boton in self.botones:
			self.botones[boton].cambiar_color(self.pos_mouse)
	
	# Crear función para controlar los eventos de los botones
	def eventos_buttons(self):
		for boton in self.botones:
			# Si el mouse está tocando el botón
			if self.botones[boton].presionado:
				# Poner sonido del botón
				Thread(target=self.botones[boton].sonidos[1].play).start()
				match boton:
					# Si apreto el botón de salir, apagar el juego
					case 'quit':
						self.juego['escena_actual'] = 'menu'
						Thread(target=self.juego['escenas']['juego'].__init__(self.juego)).start()
						# Poner música de la cueva cuando se juega la partida
						Thread(target=musicar, args=(path_menu+'music/musica_inicio.ogg',1.5)).start()
					# Poner el juego
					case 'play':
						self.juego['escena_actual'] = 'juego'
						self.juego['escenas']['juego'].inicio += get_ticks()/1000-self.inicio
						# Poner música de la cueva cuando se juega la partida
						Thread(target=musicar, args=(path_juego+'music/musica_partida.ogg',)).start()
