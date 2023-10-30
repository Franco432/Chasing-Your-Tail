from pygame.mixer import Sound
from random import random
from sources.escenas import *
from sources.cabeza import cabeza
from sources.cola import cola
from sources.fondo import fondo

# Definir el juego
class juego():
	def __init__(self, juego) -> None:
		self.juego = juego
		# Crear variable que guardará cuánto tiempo lleva jugando
		self.inicio = 0
		# Crear sonido de derrota
		self.derrota = Sound(path_juego+'sounds/sonidos_muerte.ogg')
		# Crear sonidos de timba
		self.timba = Sound(path_juego+'sounds/sonido_timba.ogg')
		# Crear las partes del perro
		self.cabeza = cabeza(path_juego+'images/perro/')
		self.cola = cola(path_juego+'images/perro/')
		# Añadir el fondo para que lo dibuje
		self.fondo = fondo(path_juego+'images/')
		# Añadir una imagen de un conómetro para contar el tiempo
		self.cronos = imagen(path_juego+'images/interfaz/cronos.png', 0, 0, 180, 120).image
		# Añadir botón de pausa
		self.boton_pausa = buton(path_juego+'images/interfaz/pause.png', 1150, 10, 70, 70, path_juego+'sounds/sonido_posarse.ogg', path_juego+'sounds/sonido_presionar.ogg')
		# Añadir fuente de texto para cronometrar
		self.fuente_cron = SysFont('Times New Roman', 90, 0)
		self.tiempo = self.fuente_cron.render('1:05', False, (255, 240, 225))
		# Crear variable que dirá cuánto tiempo queda
		self.tiempo_restante = self.tiempo_inicial = self.tiempo_anterior = 65
		# Crear variable que dirá cuál fue la tecla que presionó el usuario por última vez
		self.tecla = 'n'

	# Controlar lo que pasa en la partida
	def funciones(self):
		# Obtener la pocisión del mouse
		self.pos_mouse = get_pos()
		# Obtener el momento del frame
		self.time = get_ticks()/1000-self.inicio
		# Controlar los botones
		Thread(target=self.boton_pausa.cambiar_color, args=(self.pos_mouse,)).start()
		# Controlar el cronómetro
		Thread(target=self.cronometro).start()
		# Controlar al perro
		Thread(target=self.perro).start()
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
		# Dibujar el cronómetro y el tiempo que queda
		screen.blit(self.cronos, (640, 20))
		screen.blit(self.tiempo, (650, 30))
		# Dibujar su botón en pantalla
		screen.blit(self.boton_pausa.image, (self.boton_pausa.x, self.boton_pausa.y))
		
		# Actualizar la pantalla
		flip()
	
	# Definir función para recibir inputs del usuario
	def eventos(self):
		for event in get():
			# Si presionó una tecla
			if event.type == KEYDOWN:
				# Inentar cambiar su tecla a una que sirva para mover al perro
				match event.key:
					case  97: self.tecla = 'a'
					case 113: self.tecla = 'q'
					case 100: self.tecla = 'd'
					case 101: self.tecla = 'e'
					case 102: self.tecla = 'f'
					case 114: self.tecla = 'r'
					case 104: self.tecla = 'h'
					case 121: self.tecla = 'y'

			# Si presionó el mouse con click izquierdo
			elif event.type == MOUSEBUTTONUP and event.button == 1:
				# Poner la pausa si apretó el botón de pausa
				if self.boton_pausa.presionado:
					self.juego['escena_actual'] = 'pausa'
					# Guardar el momento en que se puso la pausa
					self.juego['escenas']['pausa'].inicio = self.inicio+self.time
					# Poner sonido del botón
					Thread(target=self.boton_pausa.sonidos[1].play).start()
					# Poner música de la cueva cuando se juega la partida
					Thread(target=musicar, args=(path_pausa+'music/musica_pausa.ogg',1.5)).start()

			# Salir del juego
			elif event.type == QUIT: self.juego['ejecutando'] = False

	# Definir función para controlar al perro
	def perro(self):
		self.fondo.moverse(self.juego['dt'], self.time)
		# Hacer que la cabeza sepa a qué tecla tiene que cambiar
		self.cabeza.cambios(self.fondo.velocidad, self.time)
		self.cabeza.cambiar(self.tecla, self.time)
		# Hacer que el trasero del perro se mueva
		self.cola.cambiar(self.fondo.velocidad, self.time)

	# Definir función para controlar el cronómetro
	def cronometro(self):
		# Obtener el tiempo que queda para que acabe la partida
		self.tiempo_restante = round(self.tiempo_inicial-self.time)
		# Crear una surface del tiempo que queda (lógica para poner o no un 0 en los segundos)
		segundos = (self.tiempo_restante)%60
		self.tiempo = self.fuente_cron.render(f'{(self.tiempo_restante)//60}:{segundos}' if segundos > 9 else f'{(self.tiempo_restante)//60}:0{segundos}', False, (220, 240, 235) if self.tiempo_restante > 5 or (random() > 0.99) else (255, 175, 150))
		# Si el tiempo que queda es cero, poner la escena de derrota
		if self.tiempo_restante <= 0:
			# Poner sonido de derrota
			Thread(target=self.derrota.play).start()
			# Cambiar la escena a derrota
			self.juego['escena_actual'] = 'derro'
			# Poner música de la pantalla de derrota
			Thread(target=musicar, args=(path_derro+'music/musica_derrota.ogg',1.5)).start()

		# Poner sonido de tick cada vez que cambie el segundo si quedan menos de 5 segundos
		if self.tiempo_restante <= 5 and self.tiempo_anterior != self.tiempo_restante:
			Thread(target=self.timba.play).start()

		# Guardar cuál fue el segundo anterior
		self.tiempo_anterior = self.tiempo_restante
