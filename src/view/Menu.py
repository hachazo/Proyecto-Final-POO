import sys

import pygame

from .Boton import *
from .settings import *

def menu_principal():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXTO = get_fuente(120).render("HEROES DEL BALON", True, "White")
        MENU_RECT = MENU_TEXTO.get_rect(center=(int(ANCHO * 0.5), 180))

        BOTON_LOGIN = Boton(
            boton_cuadrado,
            (int(ANCHO * 0.1), int(ALTO * 0.1)),
            "👤",
            pygame.font.Font(EMOJIS, 50),
            BLANCO,
            NEGRO,
        )

        BOTON_JUGAR = Boton(
            boton_surface,
            (int(ANCHO * 0.5), int(ALTO * 0.5)),
            "JUGAR",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )
        BOTON_OPCIONES = Boton(
            boton_surface,
            (int(ANCHO * 0.5), int(ALTO * 0.5 + 180)),
            "OPCIONES",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )

        BOTON_RANKING = Boton(
            boton_surface,
            (int(ANCHO * 0.5), int(ALTO * 0.5 + 90)),
            "RANKING",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )

        BOTON_SALIR = Boton(
            boton_rojo,
            (int(ANCHO * 0.5), int(ALTO * 0.5 + 270)),
            "SALIR",
            get_fuente(75),
            BLANCO,
            ROJO,
        )

        SCREEN.blit(MENU_TEXTO, MENU_RECT)

        for boton in [
            BOTON_JUGAR,
            BOTON_OPCIONES,
            BOTON_RANKING,
            BOTON_SALIR,
            BOTON_LOGIN,
        ]:
            boton.changeColor(MENU_MOUSE_POS)
            boton.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_LOGIN.checkForInput(MENU_MOUSE_POS):
                    login()
                if BOTON_JUGAR.checkForInput(MENU_MOUSE_POS):
                    jugar()
                if BOTON_OPCIONES.checkForInput(MENU_MOUSE_POS):
                    opciones()
                if BOTON_RANKING.checkForInput(MENU_MOUSE_POS):
                    ranking()
                if BOTON_SALIR.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        clock.tick(60)
        pygame.display.update()