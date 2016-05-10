#levelLibrary.py
#Created by: Talon Henderson
#Created on: 4/13/16
'''
A library to house the level elements of the Blic program.
'''

import pygame
import playerLibrary
import platformLibrary
import toastGoal

#Change Log

#----------

class Level(object):
 
    def __init__(self, filename, screenHeight, screenWidth):
        self.platformList = pygame.sprite.Group()
        self.toastList = pygame.sprite.Group()
        
        self.background = pygame.image.load("background.png").convert()
        self.fileSchematic = open(filename, "r")
        self.levelSchematic = self.fileSchematic.read()
        self.screenHeight = screenHeight
        self.screenWidth = screenWidth
        self.playerCoords = (0,0)
 
    def update(self):
        self.platformList.update()
 
    def draw(self, screen):
        screen.blit(self.background, [0,0])
        self.platformList.draw(screen)
        self.toastList.draw(screen)

    def create(self):
        xPos = 0
        yPos = 950
        width = 0
        height = 50
        counter = 0
        filename = ""
        steps = 0
        xOrigin = 0
        for i in self.levelSchematic:
            if i == "1":
                width += 50
                if width == 50:
                    filename = "grassblock50.png"
                    steps += 1
                elif width == 100:
                    filename = "grassblock100.png"
                    steps += 1
                elif width == 150:
                    filename = "grassblock150.png"
                    steps += 1
                elif width == 200:
                    filename = "grassblock200.png"
                    steps += 1
                elif width == 250:
                    filename = "grassblock250.png"
                    steps += 1
                elif width == 300:
                    filename = "grassblock300.png"
                    steps += 1
                elif width == 350:
                    filename = "grassblock350.png"
                    steps += 1
                elif width == 400:
                    filename = "grassblock400.png"
                    steps += 1
                elif width == 450:
                    filename = "grassblock450.png"
                    steps += 1
                elif width == 500:
                    filename = "grassblock500.png"
                    floor = platformLibrary.platform(xPos, yPos, filename, steps, xOrigin)
                    self.platformList.add(floor)
                    width = 0
                    steps = 0
                    xOrigin = 0
            elif i == "3":
                self.playerCoords = (xPos, yPos)
            elif i == "0":
                if width > 0:
                    floor = platformLibrary.platform(xPos, yPos, filename, steps, xOrigin)
                    self.platformList.add(floor)
                    xOrigin = 0
                    width = 0
                    steps = 0
            elif i == "4":
                toast = toastGoal.toastGoal(xPos, yPos)
                self.toastList.add(toast)
            counter += 1
            if counter != 21:
                xPos += 50
                xOrigin += 50
            else:
                if steps != 0:
                    floor = platformLibrary.platform(xPos, yPos, filename, steps, xOrigin)
                    self.platformList.add(floor)
                counter = 0
                yPos -= 60
                xPos = 0
                xOrigin = 0
                width = 0

    def getPlayerCoords(self):
        return(self.playerCoords)
                    
