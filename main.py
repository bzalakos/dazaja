"""Run this one to run the program. May or may not actually contain the bulk of the code, but eh."""

import os
import sys
import random
import pygame
from numpy import clip

default_sprite = pygame.Surface((0,0))

def main():
    """Main entrypoint into the program
    Starts by setting up the environment, then kicks it down a hill"""
    os.chdir(os.path.dirname(__file__)) # I really shouldn't need this line, but eh, atom.
    pygame.init()
    size = width, height = 320, 240
    default_sprite = pygame.image.load('al.png')
    speed, black, screen = [2, 2], [0, 0, 0], pygame.display.set_mode(size)
    dude = pygame.image.load('100.png')
    dure = dude.get_rect()

    while True: #Terrible idea, or Best Idea?
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        dure = dure.move(speed)
        if dure.left < 0 or dure.right > width:
            speed[0] *= -1
        if dure.top < 0 or dure.bottom > height:
            speed[1] *= -1

        black = [clip(_ + (random.random()*2 - 1), 0, 255) for _ in black]
        screen.fill(black)
        screen.blit(dude, dure)
        pygame.display.flip()

class Thing:
    """Object Entity Actor, whatever, it's a thing, it might do stuff"""
    def __init__(self):
        self.position = [0,0]
        self.speed = 0
        self.sprite = default_sprite
        self.bbox = self.sprite.get_rect()  # #rekt

    def step(self, delta):
        """Do a little bit of thing, delta is time since last step"""
        pass

    def draw(self, screen: pygame.Surface):
        """May or may not want to overwrite this, iono"""
        screen.blit(self.sprite, self.bbox)

class MyDude(Thing):
    """It is Wednesday."""
    def __init__(self):
        self.speed = 2

    def step(self, delta: float):
        """Do part of a thing
        Keep track of how long it's been since the last part, so you know how much of it to do"""
        keys = pygame.key.get_pressed() # Take a snapshot of the keyboard
        if keys[pygame.K_LEFT]:
            self.position[0] -= delta * self.speed


if __name__ == '__main__':
    main()
