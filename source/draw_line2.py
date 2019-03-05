""" draw_line2.py """
import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        SURFACE.fill((0,0,0))

        #白:縦線
        for xpos in range(0, 400, 25):
            pygame.draw.line(SURFACE, 0xffffff, (xpos, 0), (xpos, 300))
        #白:横線
        for ypos in range(0, 300, 25):
            pygame.draw.line(SURFACE, 0xffffff, (0, ypos), (400, ypos))
        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()
