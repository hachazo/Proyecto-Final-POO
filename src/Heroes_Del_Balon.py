import sys
import pygame as pg
from controller.Controller import Controllervista
from controller.Iniciar_pygame import Pygame_loader

if __name__ == "__main__":
    
    app = Controllervista()
    loader = Pygame_loader()
    loader.iniciar_pygame()
    loader.cargar_musica()
    app.menu_principal()
    pg.quit()
    sys.exit()
