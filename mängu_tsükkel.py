from ast import Global
import time
import sys
import pygame
import os
from värvid import *
from abifunktsioonid import * 
from nupp import nupufunktsioon
import random
pygame.font.init()

base_font=pygame.font.SysFont('comicsansms',40)
user_text=''
input_rect=pygame.Rect(50,350,400,50)
color='lightgray'

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
background= pygame.image.load('background.jpg')
font = pygame.font.SysFont("comicsansms",30)
small_font = pygame.font.SysFont("comicsansms",20)
big_font = pygame.font.SysFont("comicsansms",40)


def esimene_küsimus():
    global kord
    global punktid
    global start_time
    global valikud
    global järjend
    global sõnastik
    järjend,sõnastik=info()
    start_time=time.time()
    punktid=0
    kord=0

    valikud=valik(len(järjend)-1)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        screen.blit(background,(0,0))
        display_text(screen,"Pick your question",(80,120),big_font,white)

        nupufunktsioon("1",60,200,100,40,gray,lightgray,küsimus1)
        nupufunktsioon("2",200,250,100,40,gray,lightgray,küsimus2)
        nupufunktsioon("3",340,200,100,40,gray,lightgray,küsimus3)

        
        pygame.display.update()
        clock.tick(60)

def lõpuekraan():
    current_time=time.time()
    lõplik_aeg=current_time-start_time
    tulemus=convert(lõplik_aeg)
    font=pygame.font.SysFont('comicsansms',30)
    if lõplik_aeg<=60:
        aja_boonus=5000
    else:
        aja_boonus=round(5000-lõplik_aeg*10)
    kogu_punktid=punktid+aja_boonus
    
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(background,(0,0))
        display_text(screen,f"Time:{tulemus}",(150,50),font,white)
        display_text(screen,f"Points for answers:{punktid}",(80,110),font,white)
        display_text(screen,f"Time bonus:{aja_boonus}",(120,170),font,white)
        display_text(screen,f"Total score:{kogu_punktid}",(115,230),font,white)
        nupufunktsioon("Try again",150,350,200,30,gray,lightgray,esimene_küsimus)
        nupufunktsioon("Quit",200,400,100,30,red,lightred,pygame.quit)

        pygame.display.update()
        clock.tick(60)

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
        display_text(screen,"Pick your question",(80,120),big_font,white)

        i=kord
        if i>9:
            lõpuekraan()
        elif i%3==0 and i!=0:
            nupufunktsioon("1",25,200,450,40,gray,lightgray,küsimus1)
            nupufunktsioon("2",125,250,350,40,gray,lightgray,küsimus2)
            nupufunktsioon("3",225,300,250,40,gray,lightgray,küsimus3)

        elif i%2==0:
            nupufunktsioon("1",60,200,100,40,gray,lightgray,küsimus1)
            nupufunktsioon("2",200,250,100,40,gray,lightgray,küsimus2)
            nupufunktsioon("3",340,200,100,40,gray,lightgray,küsimus3)

        else:
            nupufunktsioon("1",20,200,420,40,gray,lightgray,küsimus1)
            nupufunktsioon("2",60,300,420,40,gray,lightgray,küsimus2)
            nupufunktsioon("3",20,400,420,40,gray,lightgray,küsimus3)
        
        pygame.display.update()
        clock.tick(60)

def küsimus1():
    indeks=0
    tekst=järjend[valikud[indeks]]
    järjend.remove(tekst)
    global user_text
    global kord
    global punktid
   
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
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
                        gameloop()
                else:
                    user_text+=event.unicode
        screen.blit(background,(0,0))
        display_text(screen,tekst,(20,20),small_font,white)
        pygame.draw.rect(screen, color, input_rect)
        text_surface=base_font.render(user_text,True,('black'))

        screen.blit(text_surface,(input_rect.x+5,input_rect.y-5))
    
        pygame.display.update()
        clock.tick(60)

def küsimus2():
    indeks=1
    tekst=järjend[valikud[indeks]]
    järjend.remove(tekst)
    global user_text
    global kord
    global punktid
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
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
                        gameloop()
                else:
                    user_text+=event.unicode
        screen.blit(background,(0,0))
        display_text(screen,tekst,(20,20),small_font,white)
        pygame.draw.rect(screen, color, input_rect)
        text_surface=base_font.render(user_text,True,('black'))

        screen.blit(text_surface,(input_rect.x+5,input_rect.y-5))
    
        pygame.display.update()
        clock.tick(60)

def küsimus3():
    indeks=2
    tekst=järjend[valikud[indeks]]
    järjend.remove(tekst)
    global user_text
    global kord
    global punktid
   
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
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
                        gameloop()
                else:
                    user_text+=event.unicode
        screen.blit(background,(0,0))
        display_text(screen,tekst,(20,20),small_font,white)
        pygame.draw.rect(screen, color, input_rect)
        text_surface=base_font.render(user_text,True,('black'))

        screen.blit(text_surface,(input_rect.x+5,input_rect.y-5))
    
        pygame.display.update()
        clock.tick(60)