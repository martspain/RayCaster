import pygame
from menu import *
from msmath import sin, cos, pi

class Game(object):
    def __init__(self, width = 1000, height = 500):
        pygame.init()
        self.rayCaster = None
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.width, self.height = width, height
        self.display = pygame.Surface((self.width, self.height))
        self.window = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.HWACCEL )
        self.fontName = "Arial"
        self.font = pygame.font.SysFont("Arial", 25)
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

    def updateFPS(self):
        fps = str(int(self.clock.get_fps()))
        fps = self.font.render(fps, 1, pygame.Color("white"))
        return fps
    
    def gameLoop(self):
        while self.playing:
            self.checkEvents()
            
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)

            #self.drawText('Thanks for playing', 25, self.width/2, self.height/2)
            self.window.fill(pygame.Color("gray"))

            # Techo
            self.window.fill(pygame.Color("saddlebrown"), (int(self.width / 2), 0,  int(self.width / 2), int(self.height / 2)))

            # Piso
            self.window.fill(pygame.Color("dimgray"), (int(self.width / 2), int(self.height / 2),  int(self.width / 2), int(self.height / 2)))


            self.rayCaster.render()

            #FPS
            self.window.fill(pygame.Color("black"), (0,0,30,30) )
            self.window.blit(self.updateFPS(), (0,0))
            self.clock.tick(60)


            pygame.display.flip()

            # self.window.blit(self.display, (0,0))
            # pygame.display.update()
            self.resetKeys()

    def checkEvents(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False

            elif ev.type == pygame.KEYDOWN:

                if ev.key == pygame.K_ESCAPE:
                    self.running, self.playing = False, False
                    self.curr_menu.run_display = False
                elif ev.key == pygame.K_RETURN:
                    self.START_KEY = True
                elif ev.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                elif ev.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                elif ev.key == pygame.K_UP:
                    self.UP_KEY = True

            
                newX = self.rayCaster.player['x']
                newY = self.rayCaster.player['y']
                forward = self.rayCaster.player['angle'] * pi / 180
                right = (self.rayCaster.player['angle'] + 90) * pi / 180

                if ev.key == pygame.K_ESCAPE:
                    self.running, self.playing = False, False
                elif ev.key == pygame.K_w:
                    newX += cos(forward) * self.rayCaster.stepSize
                    newY += sin(forward) * self.rayCaster.stepSize
                elif ev.key == pygame.K_s:
                    newX -= cos(forward) * self.rayCaster.stepSize
                    newY -= sin(forward) * self.rayCaster.stepSize
                elif ev.key == pygame.K_a:
                    newX -= cos(right) * self.rayCaster.stepSize
                    newY -= sin(right) * self.rayCaster.stepSize
                elif ev.key == pygame.K_d:
                    newX += cos(right) * self.rayCaster.stepSize
                    newY += sin(right) * self.rayCaster.stepSize
                elif ev.key == pygame.K_q:
                    self.rayCaster.player['angle'] -= self.rayCaster.turnSize
                elif ev.key == pygame.K_e:
                    self.rayCaster.player['angle'] += self.rayCaster.turnSize

                i = int(newX/self.rayCaster.blocksize)
                j = int(newY/self.rayCaster.blocksize)

                if self.rayCaster.map[j][i] == ' ':
                    self.rayCaster.player['x'] = newX
                    self.rayCaster.player['y'] = newY
    
    def resetKeys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def drawText(self, text, size, x, y):
        font = pygame.font.SysFont(self.fontName, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)