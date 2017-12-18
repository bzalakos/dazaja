"""Run this one to run the program. May or may not actually contain the bulk of the code, but eh."""

import os
import sys
import time
import pygame
os.chdir(os.path.dirname(__file__)) # I really shouldn't need this line, but eh, atom.
import sprites

def main():
    """Main entrypoint into the program
    Starts by setting up the environment, then kicks it down a hill"""
    pygame.init()
    size = width, height = 320, 240
    speed, black, screen = [2, 2], [0, 0, 0], pygame.display.set_mode(size)
    the = MyDude()
    

    while True: #Terrible idea, or Best Idea?
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

        black = [clip(_ + (random.random()*2 - 1), 0, 255) for _ in black]
        screen.fill(black)

        the.step()
        the.draw(screen)
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
        super().__init__(self)
        self.speed = 2
        self.sprite = sprites.dude
        self.bbox = sprites.dure

    def step(self, delta: float):
        """Do part of a thing
        Keep track of how long it's been since the last part, so you know how much of it to do"""
        keys = pygame.key.get_pressed() # Take a snapshot of the keyboard
        if keys[pygame.K_LEFT]:
            self.position[0] -= delta * self.speed
        if keys[pygame.K_RIGHT]:
            self.position[0] += delta * self.speed

        dure.x,dure.y = self.position

if __name__ == '__main__':
    main()
