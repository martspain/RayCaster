import pygame

class Menu(object):
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.width/2, self.game.height/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100
    
    def drawCursor(self):
        self.game.drawText('*', 15, self.cursor_rect.x, self.cursor_rect.y)
    
    def blitScreen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.resetKeys()
    
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.exitx, self.exity = self.mid_w, self.mid_h + 90

        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def displayMenu(self):
        self.run_display = True
        while self.run_display:
            self.game.checkEvents()

            self.checkInput()

            self.game.display.fill(self.game.BLACK)
            self.game.drawText('Main Menu', 20, self.mid_w, self.mid_h - 20)
            self.game.drawText('Start Game', 20, self.startx, self.starty)
            self.game.drawText('Options', 20, self.optionsx, self.optionsy)
            self.game.drawText('Credits', 20, self.creditsx, self.creditsy)
            self.game.drawText('Exit Game', 20, self.exitx, self.exity)
            self.drawCursor()

            self.blitScreen()
    
    def moveCursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
    
    def checkInput(self):
        self.moveCursor()

        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Exit':
                self.game.running = False
                self.game.playing = False
            
            self.run_display = False

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
    
    def displayMenu(self):
        self.run_display = True
        while self.run_display:
            self.game.checkEvents()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.drawText('Credits', 20, self.mid_w, self.mid_h - 20)
            self.game.drawText('Made by Martspain', 15, self.mid_w, self.mid_h + 10)
            self.blitScreen()