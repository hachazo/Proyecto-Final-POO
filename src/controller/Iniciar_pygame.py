import pygame
from view.settings import *

class Pygame_loader:
        
    def iniciar_pygame():
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
    
    def cargar_musica():
        pygame.mixer.music.load(SONIDO_FONDO)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)