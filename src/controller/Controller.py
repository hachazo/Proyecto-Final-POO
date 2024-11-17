from view.Menu import *
from view.Menu import *
from view.Boton import *

class Controllervista:
    
    def event_mouse(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Menu.BOTON_LOGIN.checkForInput(MENU_MOUSE_POS):
                    pass
                    #login()
                if Menu.BOTON_JUGAR.checkForInput(MENU_MOUSE_POS):
                    pass
                    #jugar()
                if Menu.BOTON_OPCIONES.checkForInput(MENU_MOUSE_POS):
                    pass
                    #opciones()
                if Menu.BOTON_RANKING.checkForInput(MENU_MOUSE_POS):
                    pass
                    #ranking()
                if Menu.BOTON_SALIR.checkForInput(MENU_MOUSE_POS):
                    return 0
                
        clock.tick(60)
        pygame.display.update()
    
    def menu_principal(self):
        while 1:
            if self.event_mouse() == 0:
                return
            Menu.menu_principal()
        