import time
import sys
import pygame
import os
from värvid import *
from tekstipind import *
from valikud import *
from nupp import nupufunktsioon
pygame.init()


pygame.display.set_caption("projekt")
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        font = pygame.font.Font(None,100)
        textSurface, textRect = text_objects("Pealkiri", font)
        textRect.center = (500/2,500/2)
        screen.blit(textSurface, textRect)
    
       
        nupufunktsioon("Alusta",220,300,100,30,darkblue, lightblue,gameloop)
        nupufunktsioon("Lõpeta", 220,400,100,30,darkblue,lightblue,pygame.quit)
    

        pygame.display.update()
        clock.tick(15)

def gameloop():
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        font = pygame.font.Font(None,100)
        textSurface, textRect = text_objects("Vali oma tee", font)
        textRect.center = (250,100)
        screen.blit(textSurface, textRect)
        pygame.display.update()
        clock.tick(15)

intro()
