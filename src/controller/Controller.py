from view.Menu import *
from view.settings import *
class Controllervista:
    def __init__(self):
        self.__menu_principal = menu_principal()
        
    def menu_principal(self):
        self.__menu_principal.menu_principal()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BOTON_LOGIN.checkForInput(MENU_MOUSE_POS):
                        pass
                        #login()
                    if BOTON_JUGAR.checkForInput(MENU_MOUSE_POS):
                        pass
                        #jugar()
                    if BOTON_OPCIONES.checkForInput(MENU_MOUSE_POS):
                        pass
                        #opciones()
                    if BOTON_RANKING.checkForInput(MENU_MOUSE_POS):
                        pass
                        #ranking()
                    if BOTON_SALIR.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
        clock.tick(60)
        pygame.display.update()