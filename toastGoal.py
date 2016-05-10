#toastGoal.py
#Created by: Talon Henderson - TH
#Created on: 4/12/16
'''
A program to house the creation of the taost level goal
'''

import pygame

#Change Log

#----------

class toastGoal(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("toast.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
