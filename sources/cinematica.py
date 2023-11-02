from sources.escenas import *
from pygame import K_RETURN, K_SPACE, K_RIGHT

# Definir la cinemática
class cinematica():
	def __init__(self, juego) -> None:
		self.juego = juego
		# Crear grupo que contendrá sus imágenes
		self.grupo = Group()
		# Crearse diapositivas
		self.crear_diapositivas(0)
		self.fondo = imagen(path_cinem+'images/'+self.diapositivs[self.num_diapositiva][1]+'.jpg', 0, 0, 1280, 720)
		# Crearse las fuente de texto
		self.font = SysFont('candara', 40, True)
		# Añadir el fondo para que lo dibuje
		self.grupo.add(self.fondo)
		# Añadir botón de salir
		self.boton_salir = buton(path_cinem+'images/exit.png', 1150, 10, 100, 60, path_cinem+'sounds/son.ogg', path_cinem+'sounds/son.ogg')
		self.grupo.add(self.boton_salir)
	
	# Crear función para reiniciar sus diapositivas
	def crear_diapositivas(self, cambiar=1):
		# Crear la ruta al sonido de los dialogos
		sonido_dialogo = path_cinem+'sounds/dialogue_sound.ogg'
		# Crear muchos dialogos, junto a sus pocisiones y sus backgrounds correspondientes
		self.diapositivs = (
			((dialogo('This is ghosty,\nthe phantom dog.\n->', sonido_dialogo), dialogo('My family adopted it\nsome hundreds of years ago.\n->', sonido_dialogo)), 'fondo', (200, 150)),
			((dialogo('It loves chasing\nits tail and trying\nto bite it.\n->', sonido_dialogo), dialogo('Help it\nwith that!\n->', sonido_dialogo)), 'fondo', (350, 100)), 
		)
		# Iniciar con los índices en 0
		self.num_diapositiva = self.num_texto = 0
		# Aquí se hace una condición para no intentar cambiar el fondo al crear el fondo
		if cambiar: self.fondo.cambiar_imagen(path_cinem+'images/'+self.diapositivs[self.num_diapositiva][1]+'.jpg', 0, 0, 1280, 720)

	# Controlar lo que pasa en la partida
	def funciones(self):
		# Obtener la pocisión del mouse
		self.pos_mouse = get_pos()
		# Controlar los botones
		Thread(target=self.boton_salir.cambiar_color, args=(self.pos_mouse,)).start()
		# Controlar sus textos y diapositivas
		self.dialogos()
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
		# Imprimir en pantalla las nuevas oraciones
		self.diapositivs[self.num_diapositiva][0][self.num_texto].mostrar_texto(self.diapositivs[self.num_diapositiva][2][0], self.diapositivs[self.num_diapositiva][2][1], (150, 175, 230), self.font, self.juego['screen'])
		# Actualizar la pantalla
		flip()
	
	# Definir función para recibir inputs del usuario
	def eventos(self):
		for event in get():
			# Cambiar de texto si el jugador apreta enter o espacio
			if event.type == KEYDOWN and (event.key in {K_RETURN, K_SPACE, K_RIGHT}):
				self.diapositivas()

			# Si presionó el mouse con click izquierdo
			elif event.type == MOUSEBUTTONUP and event.button == 1:
				# Poner el menú si apretó el botón de salir
				if self.boton_salir.presionado:
					self.juego['escena_actual'] = 'menu'
					# Reiniciar sus diapositivas
					self.crear_diapositivas()
					# Poner música de la cueva cuando se juega la partida
					Thread(target=musicar, args=(path_menu+'music/musica_inicio.ogg',1.5)).start()
				# Cambiar de diapositiva
				else: target=self.diapositivas()

			# Salir del juego
			elif event.type == QUIT: self.juego['ejecutando'] = False

	# Definir función para controlar las diapositivas
	def dialogos(self):
		# Añadirle letras a su diálogo actual
		self.diapositivs[self.num_diapositiva][0][self.num_texto].cambiar_letra(get_ticks()/1000,)

	# Definir función para controlar las diapositivas
	def diapositivas(self):
		# Cambiar de texto a mostrar
		self.num_texto += 1
		# Cambiar la diapositiva si se terminaron los textos
		try: self.diapositivs[self.num_diapositiva][0][self.num_texto]
		except:
			self.num_diapositiva += 1
			# Ver si tiene que comenzar el juego si se terminaron las diapositivas
			try:
				self.diapositivs[self.num_diapositiva]
				self.num_texto = 0
				self.fondo.cambiar_imagen(path_cinem+'images/'+self.diapositivs[self.num_diapositiva][1]+'.jpg', 0, 0, 1280, 720)
			except:
				# Reiniciar sus diapositivas
				self.crear_diapositivas()
				# Cambiar la escena al juego
				self.juego['escena_actual'] = 'juego'
				# Poner la música del juego
				Thread(target=musicar, args=(path_juego+'music/musica_partida.ogg',)).start()
