#platform.py
#Created by: Talon Henderson - TH
#Created on: 4/11/16
'''
A program to house the creation of platform objects.
'''

import pygame

GRASS = (137, 234, 96)

#Change Log

#----------

class platform(pygame.sprite.Sprite):

    def __init__(self, x, y, fileName, steps, xOrigin):
        super().__init__()
        self.image = pygame.image.load(fileName).convert()
        self.rect = self.image.get_rect()
        self.subtractor = xOrigin / steps
        self.rect.x = x - self.subtractor - 397
        self.rect.y = y
