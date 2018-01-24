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
    the = MyDude(80, 120)
    blocks = [Square(0, 220), Square(160, 120), Square(64, 220)]
    sigma = time.time()

    while True: #Terrible idea, or Best Idea?
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                sys.exit()
        sig = time.time()
        screen.fill((0, 0, 0))

        the.step(sig - sigma, [b.bbox for b in blocks])
        the.draw(screen)
        for block in blocks: block.draw(screen)
        pygame.display.flip()
        sigma = sig

class Thing:
    """Object Entity Actor, whatever, it's a thing, it might do stuff"""
    def __init__(self, x: int = 0, y: int = 0, sprite=sprites.default_sprite):
        self.velocity = [0, 0]
        self.sprite = sprite
        self.bbox = self.sprite.get_rect()  # #rekt
        self.bbox.x, self.bbox.y = x, y

    def step(self, delta):
        """Do a little bit of thing, delta is time since last step"""
        pass

    def draw(self, screen: pygame.Surface):
        """May or may not want to overwrite this, iono"""
        screen.blit(self.sprite, self.bbox)

class MyDude(Thing):
    """It is Wednesday."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, sprite=sprites.dude, **kwargs)
        self.speed = 128
        self.jhei = 128
        self.inje = False
        self.jbegin = self.bbox.y

    def step(self, delta: float, blocks: list):
        """Do part of a thing
        Keep track of how long it's been since the last part, so you know how much of it to do"""
        keys = pygame.key.get_pressed() # Take a snapshot of the keyboard
        desp = delta * self.speed

        dote = self.bbox.move((0, 1)).collidelistall(blocks)
        ute = self.bbox.move((0, -1)).collidelistall(blocks)
        if keys[pygame.K_UP]:
            if dote and not ute:
                self.inje = True
                self.jbegin = self.bbox.y
                self.bbox.y -= desp
            if ute or self.bbox.y < self.jbegin - self.jhei:
                self.inje = False
                self.bbox.y += desp
        else:
            self.inje = False
            if dote:
                self.bbox.y = min([blocks[d].top for d in dote]) - self.bbox.h
            else:
                self.bbox.y += desp

        if keys[pygame.K_LEFT]:
            lete = self.bbox.move((-1, 0)).collidelistall(blocks)
            if lete:
                self.bbox.x = max([blocks[l].right for l in lete if abs(blocks[l].right - self.bbox.left) <= 1])
            else:
                self.bbox.x -= desp
        if keys[pygame.K_RIGHT]:
            rite = self.bbox.move((1, 0)).collidelistall(blocks)
            if rite:
                self.bbox.x = min([blocks[r].left for r in rite if abs(blocks[r].left - self.bbox.right) <= 1]) - self.bbox.w
            else:
                self.bbox.x += desp

class Square(Thing):
    """Solid Object, one would presume"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, sprite=sprites.square, **kwargs)

if __name__ == '__main__':
    main()
