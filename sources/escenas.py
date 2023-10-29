from sources.buton import buton
from sources.imagen import imagen
from sources.dialogo import dialogo
from pygame import QUIT, MOUSEBUTTONUP, KEYDOWN
from pygame.sprite import Group
from pygame.mouse import get_pos
from pygame.time import get_ticks
from pygame.display import flip
from pygame.event import get
from pygame.mixer import music
from pygame.font import SysFont
from threading import Thread

path = "/Chasing-Your-Tail/assets/"
path_juego = path + 'game/'
path_menu  = path + 'menu/'
path_pausa = path + 'pausa/'
path_cinem = path + 'cinem/'
path_derro = path + 'derro/'

# Create function to change and play music in cualquier scene
def musicar(cancion:str, segundo:float=0):
	music.load(cancion)
	music.play(-1)
	music.set_pos(segundo)
