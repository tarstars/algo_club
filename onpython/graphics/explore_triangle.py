import pygame

mx=100
my=500
pygame.display.set_mode((mx,my))
surf=pygame.display.get_surface()

for t in range(1000):
    for p in range(0,mx):
        for q in range(0,my):
            c = (0, 0, 0)
            if ((p+t) & q) == 0:
                c = (255, 255, 255)
            surf.set_at((p,q), c)
    pygame.display.update()
