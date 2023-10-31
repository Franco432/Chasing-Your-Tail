from sources.imagen import imagen

class cabeza():
	def __init__(self, ruta) -> None:
		# Crear tuplas con todos los frames de las animaciones que va a tener
		sprites = (
			(ruta+'cabeza_boc_a.png', 256, 540),
			(ruta+'cabeza_boc_d.png', 256, 540),
			(ruta+'cabeza_boc_f.png', 256, 540),
			(ruta+'cabeza_boc_h.png', 256, 540),
			(ruta+'cabeza_len_a.png', 256, 540),
			(ruta+'cabeza_len_d.png', 256, 540),
			(ruta+'cabeza_len_f.png', 256, 540),
			(ruta+'cabeza_len_h.png', 256, 540),
			(ruta+'cabeza_cor_a.png', 256, 540),
			(ruta+'cabeza_cor_d.png', 256, 540),
			(ruta+'cabeza_cor_f.png', 256, 540),
			(ruta+'cabeza_cor_h.png', 256, 540),
		)
		# Crear lista con todos los frames de sus animaciones
		self.imagenes = [imagen(sprite[0], 0, 0, sprite[1], sprite[2]).image for sprite in sprites]
		# Guardar su imagen actual como la superficie de su primer frame
		self.image = self.imagenes[0]
		# Crear variable que guarde su pocición en pantalla
		self.pos = [0, 50]
		# Crear variable que guarde su distancia con la cola
		self.distant = 1024
		# Definir variable que define si está sacando su lengua
		self.lengua = 0
		# Definir variable que indica si el usuario debe apretar una tecla
		self.cambio = 1
		# Definir el cowldown para cambiar de tecla y de lengua
		self.cowcam = self.cowlen = 0
		# Definir la última tecla presionada
		self.tecla = 'd'
		# Definir la tecla que debería presionar
		self.tecla_deber = 'a'
		# Definir variable que dirá si la última vez el fondo estaba yendo hacia la izquierda o derecha
		self.derecha = -1
		# Definir diccionario que diga qué tecla tiene que cambiar a cuál
		self.dic = {'a':'d', 'd':'a', 'f':'h', 'h':'f', 'q':'e', 'e':'q', 'r':'y', 'y':'r'}

	# Definir función para 
	def cambiar(self, tecla, time, dt):
		# Si ya llegó el momento de cambiar el estado de la lengua
		if time-self.cowlen >= 1:
			# Guardar el momento del cambio de la lengua
			self.cowlen = time
			# Si no está corriendo, hacer que solo saque o meta la lengua
			if self.lengua < 2: self.lengua = not self.lengua

		# Si la tecla que el usuario está presionando es diferente a la que había presionado la última vez
		if tecla != self.tecla:
			# Si hay que cambiar de tecla, y la tecla presionada es la que se tenía que presionar
			if self.cambio and tecla == self.tecla_deber:
				# Decir que no tiene que cambiar
				self.cambio = False
				self.tecla = tecla
				self.cowcam = time
				# Disminuir su distancia a la cola
				self.distant -= (70 if self.lengua == 2 else 35)*dt
				print(self.distant)
				# Cambiar la imagen del perro (se aplica el índice de la lengua)
				if tecla in ('h', 'y'): self.image = self.imagenes[3+self.lengua*4]
				elif tecla in ('f', 'r'): self.image = self.imagenes[2+self.lengua*4]
				elif tecla in ('d', 'e'): self.image = self.imagenes[1+self.lengua*4]
				elif tecla in ('a', 'q'): self.image = self.imagenes[0+self.lengua*4]
		
		# Aumentar su distancia de la cola si ya debió haber presionado la tecla, dependiendo de si está corriendo o no
		if ((self.lengua == 2 and time-self.cowcam > 0.3) or (time-self.cowcam > 0.6)) and self.distant < 1024:
			self.distant += 1*dt
		
		# Cambiar su pocisión en la pantalla según si está yendo hacia la derecha o caminando y qué tan cerca está del perro
		self.pos[0] = (1024-self.distant) if self.derecha else (self.distant)

	# Definir función para saber cuándo debe cambiar de animación
	def cambios(self, vel_fondo, time):
		# Si la dirección del fondo es diferente a la guardada
		if (vel_fondo < 0) != self.derecha or (self.lengua != 2) != (abs(vel_fondo) < 100):
			# Cambiar su guardado de dirección
			self.derecha = (vel_fondo < 0)
			# Definir con la lengua si está corriendo o caminando
			self.lengua = 0 if abs(vel_fondo) < 100 else 2
			# Cambiar su imagen y sus teclas de acuerdo a su dirección y velocidad
			if self.derecha:
				# Si está corriendo
				if self.lengua == 2:
					self.tecla_deber = 'q'
					self.tecla = 'e'
				# Si está caminando
				else:
					self.tecla_deber = 'a'
					self.tecla = 'd'
				# Cambiar su imagen
				self.image = self.imagenes[0+self.lengua*4]
			else:
				# Si está corriendo
				if self.lengua == 2:
					self.tecla_deber = 'r'
					self.tecla = 'y'
				# Si está caminando
				else:
					self.tecla_deber = 'f'
					self.tecla = 'h'
				# Cambiar su imagen
				self.image = self.imagenes[2+self.lengua*4]

		# Si no está cambiando la tecla y el momento de cambiar de tecla ya llegó
		if not self.cambio and time-self.cowcam > 0.1:
			# Guardar que sí tiene que cambiar
			self.cambio = True
			# Decidir cuál tecla debe presinar ahora
			self.tecla_deber = self.dic[self.tecla]
