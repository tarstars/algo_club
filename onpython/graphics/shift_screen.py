#!/usr/bin/python

import pygame
import math
mx=1400
my=900
pygame.display.set_mode((mx,my))
surf=pygame.display.get_surface()

def triangle():
    for t in range(mx):
        p = mx-1
        for q in range(0,my):
            c = (0, 0, 0)
            if ((p+t) & q) == 0:
                c = (255, 255, 255)
            surf.set_at((p,q), c)
        surf.blit(surf, (-1, 0))
        pygame.display.update()

def circle():        
    cx=mx/2
    cy=my/2
    for t in range(1):
        for p in range(0,mx):
            for q in range(0,my):
                dx=p-cx
                dy=q-cy
                v=int(255*(1+math.cos((math.sqrt(dx**2+dy**2)+t)/2))/2)
                c = (v, v, v)
                surf.set_at((p,q), c)
            pygame.display.update()

for t in range(10):
    triangle()
    circle()
