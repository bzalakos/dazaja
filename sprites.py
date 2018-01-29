"""Put all the graphics loading in here, then import it from the main, boom: instant Global State"""
import pygame

# Not bothered by invalid constant names, don't much care for ALL CAPS. pylint: disable=C0103
default_sprite = pygame.image.load('al.png')
square = pygame.image.load('square.png')
dude = pygame.image.load('100.png')
scissor = pygame.image.load('blankscissor.png')
