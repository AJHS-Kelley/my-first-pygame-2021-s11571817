# PyGame Practice, Caile Harden, 12/1/21 8:37am, v0.6

import pygame, sys
from pygame.locals import *

# start PyGame
pygame.init()

# Create game window
windowSurface = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Hello, World")

# Set Color Values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAROON = (128, 0, 0)
PERIWINKLE = (179, 179, 255)
SAGE = (159, 223, 159)

# Setup Fonts
basicFont = pygame.font.SysFont(None,48)

# SetUp Text
text = basicFont.render('Hello, World', True, WHITE, BLUE) 
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Draw Background onto window surface
windowSurface.fill(PERIWINKLE)

# Draw a green polygon onto the surface
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Draw blue lines on the windows surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# Draw a rec circle
pygame.draw.circle(windowSurface, RED, (300, 50), 20, 0)

#Draw an ellipse
pygame.draw.ellipse(windowSurface, MAROON, (300, 250, 40, 80), 1)

# Draw a text background rectangle onto surface
pygame.draw.rect(windowSurface, BLUE, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = SAGE
del pixArray

# Draw the text onto the surface
windowSurface.blit(text, textRect)




