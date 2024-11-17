from view.Menu import *
from view.settings import *

class Controllervista:
    # def __init__(self):
    #     self.__menu_principal = menu_principal()
        
    def iniciar_pygame():
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
    
    def cargar_musica():
        pygame.mixer.music.load(SONIDO_FONDO)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def event_mouse(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
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
    
    def menu_principal(self):
        while 1:
            if self.event_mouse() == 0:
                return
            self.pygame_setup()
            self.cargar_musica()
            Menu.menu_principal()
        