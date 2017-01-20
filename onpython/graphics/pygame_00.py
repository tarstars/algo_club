import pygame

pygame.display.set_mode((400,300))
surf=pygame.display.get_surface()
pygame.draw.circle(surf,(255,255,255),(100, 100), 50)
pygame.display.update()
