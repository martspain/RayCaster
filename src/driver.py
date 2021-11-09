import pygame
from msmath import cos, sin, pi
from raycaster import Raycaster
from game import Game

RAY_AMOUNT = 100

width = 500
height = 500

g = Game(width, height)

rCaster = Raycaster(g.window)

rCaster.ray_amount = RAY_AMOUNT
rCaster.load_map("res/maps/map.txt")

wallcolors = {
    '1': pygame.Color('red'),
    '2': pygame.Color('green'),
    '3': pygame.Color('blue'),
    '4': pygame.Color('yellow'),
    '5': pygame.Color('purple')
}

wallTextures = {
    '1': pygame.image.load('res/textures/wall1.png').convert(),
    '2': pygame.image.load('res/textures/wall2.png').convert(),
    '3': pygame.image.load('res/textures/wall3.png').convert(),
    '4': pygame.image.load('res/textures/wall4.png').convert(),
    '5': pygame.image.load('res/textures/wall5.png').convert()
    }

rCaster.wallTextures = wallTextures

g.rayCaster = rCaster

while g.running:
    g.curr_menu.displayMenu()
    g.gameLoop()

pygame.quit()