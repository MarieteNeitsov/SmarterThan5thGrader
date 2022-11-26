import time
import pygame
import os
from värvid import *
from tekstipind import *
from valikud import *
from nupp import *
pygame.init()

pygame.display.set_caption("projekt")
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

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

        valikud=valik()
        button("1",185,300,120,20,valikud[0])
        button("2", 185,330,120,20,valikud[1])
        button("3", 185,360,120,20,valikud[2])
        pygame.display.update()
        clock.tick(15)

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
    
       
        button("Alusta",250, 100,75,20,darkblue, lightblue,gameloop)
        button("Lõpeta", 350,100,75,20,darkblue,lightblue,pygame.quit)
    

        pygame.display.update()
        clock.tick(15)
intro()
