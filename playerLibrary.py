#playerLibrary.py
#Created by: Talon Henderson - TH
#Created on: 4/12/16
'''
A library to house the class for a player character.
'''

import pygame

WHITE = (255, 255, 255)

#Change Log

#----------

class player(pygame.sprite.Sprite):
    def __init__(self, screenHeight, screenWidth):
        super().__init__()
 
        self.width = 20
        self.height = 35
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
 

        self.rect = self.image.get_rect()
        self.changeY = 0
        self.changeX = 0

        self.screenHeight = screenHeight
        self.screenWidth = screenWidth

        self.sprint = False
 
        self.level = None

        self.levelComplete = False
 
    def update(self):
        self.calculateGravity()

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 980:
            self.rect.x =  980
        else:
            self.rect.x += self.changeX
        platformHitList = pygame.sprite.spritecollide(self, self.level.platformList, False)
        for block in platformHitList:
            if self.changeX > 0:
                self.rect.right = block.rect.left
            elif self.changeX < 0:
                self.rect.left = block.rect.right

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 980:
            self.rect.y =  980
        else:
            self.rect.y += self.changeY
        platformHitList = pygame.sprite.spritecollide(self, self.level.platformList, False)
        for block in platformHitList:
            if self.changeY > 0:
                self.rect.bottom = block.rect.top
            elif self.changeY < 0:
                self.rect.top = block.rect.bottom

        toastHitList = pygame.sprite.spritecollide(self, self.level.toastList, False)
        if len(toastHitList) > 0:
            self.levelComplete = True

            self.changeY = 0

    def calculateGravity(self):
        if self.changeY == 0:
            self.changeY = 1
        else:
            self.changeY += .35

        if self.rect.y >= self.screenHeight - self.rect.height and self.changeY >= 0:
            self.changeY = 0
            self.rect.y = self.screenHeight - self.rect.height

    def jump(self):
        self.rect.y += 2
        platformHitList = pygame.sprite.spritecollide(self, self.level.platformList, False)
        self.rect.y -= 2

        if len(platformHitList) > 0 or self.rect.bottom >= self.screenHeight:
            self.changeY = -10

    def right(self):
        if self.sprint == False:
            self.changeX = 4
        else:
            self.changeX = 6

    def left(self):
        if self.sprint == False:
            self.changeX = -4
        else:
            self.changeX = -6

    def stop(self):
        self.changeX = 0

    def Sprint(self):
        self.sprint = True

    def stopSprint(self):
        self.sprint = False
