import pygame 
from pygame.locals import*
from sys import exit

class Interface:
    def __init__(self, filosofos):
        self.filosofos = filosofos
        self.comecar()

    def comecar(self):
        pygame.init()

        tela = pygame.display.set_mode((640, 480))

        pygame.display.set_caption("Jantar dos filósofos")
        while True:

            pygame.draw.circle(tela, (255, 255, 255), (320, 240), 240)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            if self.filosofos[0].estado == 1: #pensando
                pygame.draw.circle(tela, (255, 255, 0), (160, 180), 50)
            elif self.filosofos[0].estado == 2:#comendo 
                pygame.draw.circle(tela, (0, 255, 0), (160, 180), 50)
            elif self.filosofos[0].estado == 3:#faminto
                pygame.draw.circle(tela, (255, 0, 0), (160, 180), 50)

            if self.filosofos[1].estado == 1:
                pygame.draw.circle(tela, (255, 255, 0), (200, 360), 50)
            elif self.filosofos[1].estado == 2:
                pygame.draw.circle(tela, (0, 255, 0), (200, 360), 50)
            elif self.filosofos[1].estado == 3:
                pygame.draw.circle(tela, (255, 0, 0), (200, 360), 50)

            if self.filosofos[2].estado == 1:
                pygame.draw.circle(tela, (255, 255, 0), (460, 340), 50)
            elif self.filosofos[2].estado == 2:
                pygame.draw.circle(tela, (0, 255, 0), (460, 340), 50)
            elif self.filosofos[2].estado == 3:
                pygame.draw.circle(tela, (255,0 ,0), (460, 340), 50)

            if self.filosofos[3].estado == 1:
                pygame.draw.circle(tela, (255, 255, 0), (480, 180), 50)
            elif self.filosofos[3].estado == 2:
                pygame.draw.circle(tela, (0, 255, 0), (480, 180), 50)
            elif self.filosofos[3].estado == 3:
                pygame.draw.circle(tela, (255, 0, 0), (480, 180), 50)

            if self.filosofos[4].estado == 1:
                pygame.draw.circle(tela, (255, 255, 0), (320, 80), 50)
            elif self.filosofos[4].estado == 2:
                pygame.draw.circle(tela, (0, 255, 0), (320, 80), 50)
            elif self.filosofos[4].estado == 3:
                pygame.draw.circle(tela, (255,0 , 0), (320, 80), 50)

            pygame.display.update()

 