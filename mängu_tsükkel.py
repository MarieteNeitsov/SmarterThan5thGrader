from ast import Global
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

base_font=pygame.font.SysFont('comicsansms',40)
user_text=''
input_rect=pygame.Rect(50,350,400,50)
color='lightgray'
punktid=0
kord=0
start_time=0
current_time=0

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


def timer():
    start_time=pygame.time.get_ticks()
    gameloop()
   
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def gameloop():
    global valikud
    global kord
    valikud=valik(len(järjend)-1)
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
        screen.blit(textSurface, textRect)
        
       
        i=kord 
        if i%3==0 and i!=0:
            nupufunktsioon("1",25,150,50,30,darkblue,lightblue,küsimus1)
            nupufunktsioon("2",225,180,50,30,darkblue,lightblue,küsimus2)
            nupufunktsioon("3",425,210,50,30,darkblue,lightblue,küsimus3)

        elif i%2==0:
            nupufunktsioon("1",20,150,460,30,darkblue,lightblue,küsimus1)
            nupufunktsioon("2",20,200,460,30,darkblue,lightblue,küsimus2)
            nupufunktsioon("3",20,250,460,30,darkblue,lightblue,küsimus3)

        else:
            nupufunktsioon("1",20,150,440,30,darkblue,lightblue,küsimus1)
            nupufunktsioon("2",40,200,440,30,darkblue,lightblue,küsimus2)
            nupufunktsioon("3",20,250,440,30,darkblue,lightblue,küsimus3)
       
        if i>3:
            screen.blit(background,(0,0))
            current_time=pygame.time.get_ticks()
            seconds=round((current_time-start_time)/1000,1)
            result=convert(seconds)
            display_text(screen,f"Time:{result}",(200,150),font,white)
            display_text(screen,f"Your score:{punktid}",(200,200),font,white)
            

           
        pygame.display.update()
        clock.tick(60)

def küsimus1():
    indeks=0
    tekst=järjend[valikud[indeks]]
    järjend.remove(tekst)
   
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                global user_text
                global kord
                global punktid
                if event.key==pygame.K_BACKSPACE:
                    user_text=user_text[:-1]
                elif event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                    if user_text.lower()==sõnastik[tekst].lower():
                        user_text=''
                        display_text(screen,"correct!",(200,200),font,white)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        kord+=1
                        punktid+=1000
                        gameloop()
                    else:
                        user_text=''
                        display_text(screen,"wrong!",(200,200),font,white)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        punktid-=100
                        kord+=1
                        gameloop()
                else:
                    user_text+=event.unicode
        screen.blit(background,(0,0))
        font = pygame.font.SysFont("comicsansms",20)
        display_text(screen,tekst,(20,20),font,white)
        pygame.draw.rect(screen, color, input_rect)
        text_surface=base_font.render(user_text,True,('black'))

        screen.blit(text_surface,(input_rect.x+5,input_rect.y-5))
    
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
            if event.type==pygame.KEYDOWN:
                global user_text
                global kord
                global punktid
                if event.key==pygame.K_BACKSPACE:
                    user_text=user_text[:-1]
                elif event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                    if user_text.lower()==sõnastik[tekst].lower():
                        user_text=''
                        display_text(screen,"correct!",(200,200),font,white)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        kord+=1
                        punktid+=1000
                        gameloop()
                    else:
                        user_text=''
                        display_text(screen,"wrong!",(200,200),font,white)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        punktid-=100
                        kord+=1
                        gameloop()
                else:
                    user_text+=event.unicode
        screen.blit(background,(0,0))
        font = pygame.font.SysFont("comicsansms",20)
        display_text(screen,tekst,(20,20),font,white)
        pygame.draw.rect(screen, color, input_rect)
        text_surface=base_font.render(user_text,True,('black'))

        screen.blit(text_surface,(input_rect.x+5,input_rect.y-5))
    
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
            if event.type==pygame.KEYDOWN:
                global user_text
                global kord
                global punktid
                if event.key==pygame.K_BACKSPACE:
                    user_text=user_text[:-1]
                elif event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                    if user_text.lower()==sõnastik[tekst].lower():
                        user_text=''
                        display_text(screen,"correct!",(200,200),font,white)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        kord+=1
                        punktid+=1000
                        gameloop()
                    else:
                        user_text=''
                        display_text(screen,"wrong!",(200,200),font,white)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        punktid-=100
                        kord+=1
                        gameloop()
                else:
                    user_text+=event.unicode
        screen.blit(background,(0,0))
        font = pygame.font.SysFont("comicsansms",20)
        display_text(screen,tekst,(20,20),font,white)
        pygame.draw.rect(screen, color, input_rect)
        text_surface=base_font.render(user_text,True,('black'))

        screen.blit(text_surface,(input_rect.x+5,input_rect.y-5))
    
        pygame.display.update()
        clock.tick(60)