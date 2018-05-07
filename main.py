"""Run this one to run the program. May or may not actually contain the bulk of the code, but eh."""

import os
import sys
import time
import enum
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
    blocks = [Square(0, 220), Square(160, 156), Square(64, 220)]
    sigma = time.time()
    pygame.key.get_prevved = pygame.key.get_pressed()

    while True: #Terrible idea, or Best Idea?
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT or eve.type == pygame.KEYDOWN and eve.key == pygame.K_ESCAPE:
                sys.exit()
        sig = time.time()
        screen.fill((0, 0, 0))

        the.step(sig - sigma, [b.bbox for b in blocks])
        the.draw(screen)
        for block in blocks: block.draw(screen)
        pygame.display.flip()
        sigma = sig
        pygame.key.get_prevved = pygame.key.get_pressed()

class Thing:
    """Object Entity Actor, whatever, it's a thing, it might do stuff"""
    def __init__(self, x: int = 0, y: int = 0, sprite=sprites.default_sprite):
        self.velocity = [0, 0]
        self.sprite = sprite
        self.bbox = self.sprite.get_rect()  # #rekt
        # Yes, you do need this. BBOX uses integer coordinates, you keep insisting on floats.
        self.x_value, self.y_value = self.bbox.x, self.bbox.y = x, y
        # not sure how much of this stuff will actually be used generically
        self.tim = 0
        self.seri = {}  # Something like
        self.hse = enum.Enum('H', 'F W')
        self.xse = enum.Enum('X', 'L R')

    def get_x(self) -> float:
        """Get the current partial X position"""
        return self.x_value

    def set_x(self, value: float) -> None:
        """Set the partial X position, and update the actual X position to nearest pixel"""
        self.x_value = value
        self.bbox.x = self.x_value

    def get_y(self) -> float:
        """Get the current partial Y position"""
        return self.y_value

    def set_y(self, value: float) -> None:
        """Set the partial Y position, and update the actual Y position to nearest pixel"""
        self.y_value = value
        self.bbox.y = self.y_value

    x, y = property(get_x, set_x), property(get_y, set_y)

    def chain(self, delta):
        """Proceed through a series of timed steps, maybe"""
        the = self.seri.get(self.hse, None)
        if the:
            if self.tim <= 0:
                self.tim = the[0]
                self.hse = the[1]
            else:
                self.tim -= delta

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
        self.jpeed = self.speed * 3
        self.jhei = 65
        self.inje = False
        self.jbegin = self.bbox.y

    def step(self, delta: float, blocks: list):
        """Do part of a thing
        Keep track of how long it's been since the last part, so you know how much of it to do"""
        # Take a snapshot of the keyboard, and the state of the previous step, for comparison
        keys, peys = pygame.key.get_pressed(), pygame.key.get_prevved
        desp, jesp = delta * self.speed, delta * self.jpeed

        dote = self.bbox.move((0, 1)).collidelistall(blocks)
        ute = self.bbox.move((0, -1)).collidelistall(blocks)
        # If the key was pressed just now, and you are also on the ground and there is room to jump
        if keys[pygame.K_UP] and not peys[pygame.K_UP] and dote and not ute:
            self.inje = True    # Then begin the jump
            self.jbegin = self.bbox.bottom
        if keys[pygame.K_UP]:   # If you're just holding the button down
            if ute or self.bbox.bottom < self.jbegin - self.jhei:
                self.inje = False   # If you hit something (like your max height), no longer rising
        else:   # let go early to jump-cancel
            self.inje = False

        if dote and not self.inje:  # If on the ground and not jumping, be on the ground
            self.y = min([blocks[d].top for d in dote]) - self.bbox.h
        else:   # Otherwise, be jumping or falling, whichever the case may be
            self.y -= jesp if self.inje else -jesp

        if keys[pygame.K_LEFT]:
            lete = self.bbox.move((-1, 0)).collidelistall(blocks)
            if lete:
                self.x = max([blocks[l].right for l in lete if abs(blocks[l].right - self.bbox.left) <= 1])
            else:
                self.x -= desp
        if keys[pygame.K_RIGHT]:
            rite = self.bbox.move((1, 0)).collidelistall(blocks)
            if rite:
                self.x = min([blocks[r].left for r in rite if abs(blocks[r].left - self.bbox.right) <= 1]) - self.bbox.w
            else:
                self.x += desp

class Scissors(Thing):
    """Snippity thing"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, sprite=sprites.scissor, **kwargs)
        self.speed = 96
        self.hse = enum.Enum('H', 'F W C A R')
        self.hs = self.hse.F
        self.xs = self.xse.R
        self.seri = {'C': (0.5, self.hse.A), 'A': (0.25, self.hse.R), 'R': (0.75, self.hse.F)}

    def step(self, delta: float, blocks: list, guy: Thing):
        """Loiter, pursue, brace, strike, loiter"""
        self.chain(delta)

class Square(Thing):
    """Solid Object, one would presume"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, sprite=sprites.square, **kwargs)

if __name__ == '__main__':
    main()
