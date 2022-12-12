import time
import sys
import pygame
import os
from värvid import *
from tekstipind import *
from valikud import *
from nupp import nupufunktsioon
from info_failist import*
import random
import pygame_textinput
pygame.font.init()

base_font=pygame.font.Font(None,50)
user_text=''
input_rect=pygame.Rect(50,350,400,50)
color_active=pygame.Color('lightgray')
color_passive=pygame.Color('gray')
color=color_passive


screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
background= pygame.image.load('background.jpg')

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

def display_time(time_seconds):
  # time string with tents of seconds
  time_str =  str(int(time_seconds*10) / 10) 
  font = pygame.font.SysFont("comicsansms",50)
  label = font.render(f"Time : {time_str}", 1, red)
  screen.blit(label, (20, 20))
        
def gameloop():
    time_seconds = 0
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        screen.blit(background,(0,0))
        font = pygame.font.SysFont("comicsansms",30)
        textSurface, textRect = text_objects("Vali oma tee", font)
        textRect.center = (250,100)
        
        nupufunktsioon("1",20,100,460,30,darkblue,lightblue,küsimus1)
        nupufunktsioon("2",20,150,460,30,darkblue,lightblue,küsimus2)
        nupufunktsioon("3",20,200,460,30,darkblue,lightblue,küsimus3)

        screen.blit(textSurface, textRect)
        display_time(time_seconds)
        pygame.display.flip()

        time_millis = clock.tick(30)
        #if not game_over:
        time_seconds += time_millis / 1000
        
        pygame.display.update()
        clock.tick(60)


valikud=valik(len(järjend)-1)
active=False

def küsimus1():
    indeks=0
    tekst=järjend[valikud[indeks]]
    järjend.remove(tekst)
    #display_time(time_seconds)
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                global active
                if input_rect.collidepoint(event.pos):
                    active=True
                else:
                    active=False
            if event.type==pygame.KEYDOWN and active:
                global user_text
                if event.key==pygame.K_BACKSPACE:
                    user_text=user_text[:-1]
                elif event.key==pygame.K_RETURN:
                    if user_text.lower()==sõnastik[tekst].lower():
                        user_text=''
                        gameloop()
                    else:
                        pygame.quit()
                        quit()
                else:
                    user_text+=event.unicode
        screen.blit(background,(0,0))
        font = pygame.font.SysFont("comicsansms",20)
        display_text(screen,tekst,(20,20),font,white)
        if active:
            color=color_active
        else:
            color=color_passive

        pygame.draw.rect(screen, color, input_rect)
        text_surface=base_font.render(user_text,True,('black'))

        screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))
    
        pygame.display.update()
        clock.tick(60)

def küsimus2():
    indeks=1
    tekst=järjend[valikud[indeks]]
    järjend.remove(tekst)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                global active
                if input_rect.collidepoint(event.pos):
                    active=True
                else:
                    active=False
            if event.type==pygame.KEYDOWN and active:
                global user_text
                if event.key==pygame.K_BACKSPACE:
                    user_text=user_text[:-1]
                elif event.key==pygame.K_RETURN:
                    if user_text.lower()==sõnastik[tekst].lower():
                        user_text=''
                        gameloop()
                    else:
                        pygame.quit()
                        quit()
                else:
                    user_text+=event.unicode
        screen.blit(background,(0,0))
        font = pygame.font.SysFont("comicsansms",20)
        display_text(screen,tekst,(20,20),font,white)
        if active:
            color=color_active
        else:
            color=color_passive

        pygame.draw.rect(screen, color, input_rect)
        text_surface=base_font.render(user_text,True,('black'))

        screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))
    
        pygame.display.update()
        clock.tick(60)

def küsimus3():
    indeks=2
    tekst=järjend[valikud[indeks]]
    järjend.remove(tekst)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                global active
                if input_rect.collidepoint(event.pos):
                    active=True
                else:
                    active=False
            if event.type==pygame.KEYDOWN and active:
                global user_text
                if event.key==pygame.K_BACKSPACE:
                    user_text=user_text[:-1]
                elif event.key==pygame.K_RETURN:
                    if user_text.lower()==sõnastik[tekst].lower():
                        user_text=''
                        gameloop()
                    else:
                        pygame.quit()
                        quit()
                else:
                    user_text+=event.unicode
        screen.blit(background,(0,0))
        font = pygame.font.SysFont("comicsansms",20)
        display_text(screen,tekst,(20,20),font,white)
        if active:
            color=color_active
        else:
            color=color_passive

        pygame.draw.rect(screen, color, input_rect)
        text_surface=base_font.render(user_text,True,('black'))

        screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))
    
        pygame.display.update()
        clock.tick(60)