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
    blocks = [Square(0, 220), Square(160, 156), Square(64, 220)]
    sigma = time.time()

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

class Thing:
    """Object Entity Actor, whatever, it's a thing, it might do stuff"""
    def __init__(self, x: int = 0, y: int = 0, sprite=sprites.default_sprite):
        self.velocity = [0, 0]
        self.sprite = sprite
        self.bbox = self.sprite.get_rect()  # #rekt
        # Yes, you do need this. BBOX uses integer coordinates, you keep insisting on floats.
        self.x_value, self.y_value = self.bbox.x, self.bbox.y = x, y

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
        self.olje = False
        self.jbegin = self.bbox.y

    def step(self, delta: float, blocks: list):
        """Do part of a thing
        Keep track of how long it's been since the last part, so you know how much of it to do"""
        keys = pygame.key.get_pressed() # Take a snapshot of the keyboard
        desp, jesp = delta * self.speed, delta * self.jpeed

        dote = self.bbox.move((0, 1)).collidelistall(blocks)
        ute = self.bbox.move((0, -1)).collidelistall(blocks)
        if keys[pygame.K_UP]:
            if dote and not ute:
                if not self.olje:
                    self.inje = True
                    self.olje = True
                    self.jbegin = self.bbox.bottom
                else:
                    self.y = min([blocks[d].top for d in dote]) - self.bbox.h
            if ute or self.bbox.bottom < self.jbegin - self.jhei:
                self.inje = False
            self.y -= jesp if self.inje else -jesp
        else:
            self.inje, self.olje = False, False
            if dote:
                self.y = min([blocks[d].top for d in dote]) - self.bbox.h
            else:
                self.y += jesp

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

class Square(Thing):
    """Solid Object, one would presume"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, sprite=sprites.square, **kwargs)

if __name__ == '__main__':
    main()
