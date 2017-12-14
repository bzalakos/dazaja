"""Run this one to run the program. May or may not actually contain the bulk of the code, but eh."""

import sys
import random
import pygame
from numpy import clip

def main():
    """Main entrypoint into the program.
    Starts by setting up the environment, then kicks it down a hill."""
    pygame.init()
    size = width, height = 320, 240
    speed, black, screen = [2, 2], [0, 0, 0], pygame.display.set_mode(size)
    bal = pygame.image.load('al.png')
    balre = bal.get_rect()

    while True: #Terrible idea, or Best Idea?
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        balre = balre.move(speed)
        if balre.left < 0 or balre.right > width:
            speed[0] *= -1
        if balre.top < 0 or balre.bottom > height:
            speed[1] *= -1

        black = [clip(_ + (random.random()*2 - 1), 0, 255) for _ in black]
        screen.fill(black)
        screen.blit(bal, balre)
        pygame.display.flip()

if __name__ == '__main__':
    main()
