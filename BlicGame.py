#BlicGame.py
#Created by: Talon Henderson - TH
#Created on: 4/13/16
'''
The main game program for Blic.
'''

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

import pygame
import levelLibrary
import platformLibrary
import playerLibrary
import toastGoal

def main():
    pygame.init()
    SCREENHEIGHT = 1000
    SCREENWIDTH = 1000
    size = [SCREENWIDTH, SCREENHEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Blic Demo")
    level01 = levelLibrary.Level("level01.txt", SCREENHEIGHT, SCREENWIDTH)
    level02 = levelLibrary.Level("level02.txt", SCREENHEIGHT, SCREENWIDTH)
    player = playerLibrary.player(SCREENHEIGHT, SCREENWIDTH)
    levelsList = []
    levelsList.append(level01)
    levelsList.append(level02)
    currentLevel = 1
    currentlyPlaying = levelsList[currentLevel - 1]
    activeSpritesList = pygame.sprite.Group()
    currentlyPlaying.create()
    playerCoords = currentlyPlaying.getPlayerCoords()
    player.level = currentlyPlaying
    player.rect.x = playerCoords[0]
    player.rect.y = playerCoords[1]
    activeSpritesList.add(player)

    clock = pygame.time.Clock()

    pygame.key.set_repeat(1, 10)

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.left()
                if event.key == pygame.K_d:
                    player.right()
                if event.key == pygame.K_w:
                    player.jump()
                if event.key == pygame.K_LSHIFT:
                    player.Sprint()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.changeX < 0:
                    player.stop()
                if event.key == pygame.K_d and player.changeX > 0:
                    player.stop()
                if event.key == pygame.K_LSHIFT:
                    player.stopSprint()

        if player.levelComplete != True:
            activeSpritesList.update()
            currentlyPlaying.update()
        
            currentlyPlaying.draw(screen)
            activeSpritesList.draw(screen)
        else:
            player.levelComplete = False
            if currentLevel != 2:
                currentLevel += 1
            else:
                currentLevel = 1

            currentlyPlaying = levelsList[currentLevel - 1]

            activeSpritesList = pygame.sprite.Group()
            currentlyPlaying.create()
            playerCoords = currentlyPlaying.getPlayerCoords()
            player.rect.x = playerCoords[0]
            player.rect.y = playerCoords[1]
            player.level = currentlyPlaying
            activeSpritesList.add(player)

            activeSpritesList.update()
            currentlyPlaying.update()
        
            currentlyPlaying.draw(screen)
            activeSpritesList.draw(screen)
        
        
        
                    
        clock.tick(60)
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()
