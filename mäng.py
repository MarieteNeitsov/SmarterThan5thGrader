import time
import sys
import pygame
import os
from värvid import *
from tekstipind import *
from valikud import *
from nupp import nupufunktsioon
from info_failist import*
from mängu_tsükkel import timer
from pygame import mixer
pygame.font.init()


pygame.display.set_caption("Are you smarter than a 5th grader?")
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms",35)
background= pygame.image.load('background.jpg')

def intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        screen.blit(background,(0,0))
        display_text(screen,"Are you smarter than a 5th grader?",(60,100),font,white)
    
       
        nupufunktsioon("Start!",100,300,300,70,green,darkgreen,timer)
       
        nupufunktsioon("End Game", 150,400,200,50,red,darkred,pygame.quit)

        pygame.display.update()
        clock.tick(60)

intro()

