import time
import sys
import pygame
import os
from värvid import *
from tekstipind import *
from valikud import *
from nupp import nupufunktsioon
from info_failist import*
pygame.font.init()

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

def display_text(surface,text,pos,font,color):
    collection=[word.split(' ')for word in text.splitlines()]
    space=font.size(' ')[0]
    x,y=pos
    for lines in collection:
        for words in lines:
            words_surface=font.render(words, True, color)
            word_width,word_height=words_surface.get_size()
            if x+word_width>=500:
                x=pos[0]
                y+=word_height
            surface.blit(words_surface,(x,y))
            x+=word_width+space
        x=pos[0]
        y+=word_height


        
def gameloop():
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        font = pygame.font.SysFont("comicsansms",50)
        textSurface, textRect = text_objects("Vali oma tee", font)
        textRect.center = (250,100)
        
        nupufunktsioon("1",20,300,460,30,darkblue,lightblue,küsimus(0))
        nupufunktsioon("2",20,350,460,30,darkblue,lightblue,pygame.quit)
        nupufunktsioon("3",20,400,460,30,darkblue,lightblue,gameloop)

        screen.blit(textSurface, textRect)
        pygame.display.update()
        clock.tick(60)



        pygame.display.update()
        clock.tick(15)

def küsimus(indeks):
    valikud=valik(len(järjend)-1)
    tekst=järjend[valikud[indeks]]

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        font = pygame.font.SysFont("comicsansms",50)
        display_text(screen,tekst,(20,20),font,black)

        pygame.display.update()
        clock.tick(60)