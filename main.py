import pygame
from pygame.locals import *
FPS = 30
FramePerSec = pygame.time.Clock()
BLACK = (0,0,0)
pygame.init()
pygame.display.set_caption('Etcha - A - Sketch')
DISPLAYSURF = pygame.display.set_mode((495,406), pygame.NOFRAME)
## load and image
BG = pygame.image.load('etchasketch.jpg')
DISPLAYSURF.blit(BG, (0,0))
## DRAW CIRCLE
DRAWX = 241
DRAWY = 315

pygame.draw.circle(DISPLAYSURF, BLACK, (241, 315), 1)
def RESET():
    BG = pygame.image.load('etchasketch.jpg')
    DISPLAYSURF.blit(BG, (0, 0))
    pygame.draw.circle(DISPLAYSURF, BLACK, (241, 315), 1)

pygame.key.set_repeat(10, 10)
_RUN = True
while _RUN:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            _RUN = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                DRAWX = 241
                DRAWY = 315
                RESET()
            if event.key == pygame.K_ESCAPE:
                _RUN = False
            elif event.key == pygame.K_UP and DRAWY >= 78:
                DRAWY -= 2
                pygame.draw.circle(DISPLAYSURF, BLACK, (DRAWX, DRAWY), 1)
            elif event.key == pygame.K_LEFT and DRAWX >=79:
                DRAWX -= 2
                pygame.draw.circle(DISPLAYSURF, BLACK, (DRAWX, DRAWY), 1)
            elif event.key == pygame.K_RIGHT and DRAWX <= 417:
                DRAWX += 2
                pygame.draw.circle(DISPLAYSURF, BLACK, (DRAWX, DRAWY), 1)
            elif event.key == pygame.K_DOWN and DRAWY <= 313:
                DRAWY += 2
                pygame.draw.circle(DISPLAYSURF, BLACK, (DRAWX, DRAWY), 1)


    FramePerSec.tick(FPS)
pygame.QUIT