import pygame
from msmath import cos, sin, pi
from raycaster import Raycaster
from game import Game

RAY_AMOUNT = 100

width = 1000
height = 500

# pygame.init()
# screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL )
# screen.set_alpha(None)

g = Game()

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

# clock = pygame.time.Clock()
# font = pygame.font.SysFont("Arial", 25)

# def updateFPS():
#     fps = str(int(clock.get_fps()))
#     fps = font.render(fps, 1, pygame.Color("white"))
#     return fps

# isRunning = True

# pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

# while isRunning:

#     for ev in pygame.event.get():
#         if ev.type == pygame.QUIT:
#             isRunning = False

#         elif ev.type == pygame.KEYDOWN:
#             newX = rCaster.player['x']
#             newY = rCaster.player['y']
#             forward = rCaster.player['angle'] * pi / 180
#             right = (rCaster.player['angle'] + 90) * pi / 180

#             if ev.key == pygame.K_ESCAPE:
#                 isRunning = False
#             elif ev.key == pygame.K_w:
#                 newX += cos(forward) * rCaster.stepSize
#                 newY += sin(forward) * rCaster.stepSize
#             elif ev.key == pygame.K_s:
#                 newX -= cos(forward) * rCaster.stepSize
#                 newY -= sin(forward) * rCaster.stepSize
#             elif ev.key == pygame.K_a:
#                 newX -= cos(right) * rCaster.stepSize
#                 newY -= sin(right) * rCaster.stepSize
#             elif ev.key == pygame.K_d:
#                 newX += cos(right) * rCaster.stepSize
#                 newY += sin(right) * rCaster.stepSize
#             elif ev.key == pygame.K_q:
#                 rCaster.player['angle'] -= rCaster.turnSize
#             elif ev.key == pygame.K_e:
#                 rCaster.player['angle'] += rCaster.turnSize

#             i = int(newX/rCaster.blocksize)
#             j = int(newY/rCaster.blocksize)

#             if rCaster.map[j][i] == ' ':
#                 rCaster.player['x'] = newX
#                 rCaster.player['y'] = newY


#     screen.fill(pygame.Color("gray"))

#     # Techo
#     screen.fill(pygame.Color("saddlebrown"), (int(width / 2), 0,  int(width / 2), int(height / 2)))

#     # Piso
#     screen.fill(pygame.Color("dimgray"), (int(width / 2), int(height / 2),  int(width / 2), int(height / 2)))


#     rCaster.render()

#     #FPS
#     screen.fill(pygame.Color("black"), (0,0,30,30) )
#     screen.blit(updateFPS(), (0,0))
#     clock.tick(60)


#     pygame.display.flip()

pygame.quit()