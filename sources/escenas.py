from sources.buton import buton
from sources.imagen import imagen
from pygame.sprite import Group
from pygame.mouse import get_pos
from pygame import QUIT, MOUSEBUTTONUP
from pygame.time import get_ticks
from pygame.display import flip
from pygame.event import get
from pygame.mixer import music
from threading import Thread

path = "C:/Users/frank/Desktop/Repositorio/Proyectos_Python/Proyectos_en_curso/plantilla_juego_manyfile/assets/"
path_juego = path + 'game/'
path_menu  = path + 'menu/'
path_pausa = path + 'pausa/'

# Create function to change and play music in cualquier scene
def musicar(cancion:str, segundo:float=0):
	music.load(cancion)
	music.play(-1)
	music.set_pos(segundo)
