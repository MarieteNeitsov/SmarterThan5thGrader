import time
import sys
import pygame
import os
from värvid import *
from tekstipind import *
from valikud import *
from nupp import nupufunktsioon
from info_failist import*
from mängu_tsükkel import gameloop
pygame.font.init()


pygame.display.set_caption("Are you smarter than a 5th grader?")
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms",55)

def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        display_text(screen,"Are you smarter than a 5th grader?",(25,25),font,black)
    
       
        nupufunktsioon("Start",50,300,400,80,green, darkgreen,gameloop)
        nupufunktsioon("End Game", 150,400,200,50,red, darkred,pygame.quit)
    

        pygame.display.update()
        clock.tick(60)

intro()

