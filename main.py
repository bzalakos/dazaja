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
    size = 320, 240
    screen = pygame.display.set_mode(size)
    the = MyDude(160, 120)
    blocks = [Square(0,240), Square(64, 240), Square(128, 240)]
    sigma = time.time()

    while True: #Terrible idea, or Best Idea?
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                sys.exit()
        sig = time.time()
        screen.fill((0, 0, 0))

        the.step(sig - sigma)
        the.draw(screen)
        for block in blocks: block.draw(screen)
        pygame.display.flip()
        sigma = sig

class Thing:
    """Object Entity Actor, whatever, it's a thing, it might do stuff"""
    def __init__(self, x: int = 0, y: int = 0):
        self.position = [x, y]
        self.velocity = [0, 0]
        self.sprite = sprites.default_sprite
        self.bbox = self.sprite.get_rect()  # #rekt

    def step(self, delta):
        """Do a little bit of thing, delta is time since last step"""
        pass

    def draw(self, screen: pygame.Surface):
        """May or may not want to overwrite this, iono"""
        screen.blit(self.sprite, self.bbox)

class MyDude(Thing):
    """It is Wednesday."""
    def __init__(self, *args):
        super().__init__(args)
        self.speed = 64
        self.sprite = sprites.dude
        self.bbox = sprites.dudeb

    def step(self, delta: float):
        """Do part of a thing
        Keep track of how long it's been since the last part, so you know how much of it to do"""
        keys = pygame.key.get_pressed() # Take a snapshot of the keyboard
        if keys[pygame.K_LEFT]:
            self.position[0] -= delta * self.speed
        if keys[pygame.K_RIGHT]:
            self.position[0] += delta * self.speed

        self.bbox.x, self.bbox.y = self.position

class Square(Thing):
    """Solid Object, one would presume"""
    def __init__(self, *args):
        super().__init__(args)
        self.sprite = sprites.square
        self.bbox = sprites.squareb

if __name__ == '__main__':
    main()
