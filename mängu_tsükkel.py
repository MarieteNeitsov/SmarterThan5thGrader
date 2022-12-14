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
pygame.font.init()

base_font=pygame.font.SysFont('comicsansms',40)
user_text=''
input_rect=pygame.Rect(50,350,400,50)
color='lightgray'

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
        font = pygame.font.SysFont("comicsansms",50)
        textSurface, textRect = text_objects("Pick your question", font)
        textRect.center = (250,100)
        screen.blit(textSurface, textRect)

        nupufunktsioon("1",60,200,100,40,gray,lightgray,küsimus1)
        nupufunktsioon("2",200,250,100,40,gray,lightgray,küsimus2)
        nupufunktsioon("3",340,200,100,40,gray,lightgray,küsimus3)

        
        pygame.display.update()
        clock.tick(60)
    gameloop()

   
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def lõpuekraan():
    current_time=time.time()
    lõplik_aeg=current_time-start_time
    tulemus=convert(lõplik_aeg)
    font=pygame.font.SysFont('comicsansms',30)
    if lõplik_aeg<=60:
        aja_boonus=1000
    elif 60<lõplik_aeg<=70:
        aja_boonus=900
    elif 70<lõplik_aeg<=80:
        aja_boonus=800
    elif 80<lõplik_aeg<=90:
        aja_boonus=700
    elif 90<lõplik_aeg<=100:
        aja_boonus=600
    elif 100<lõplik_aeg<=110:
        aja_boonus=500
    elif 110<lõplik_aeg<=120:
        aja_boonus=400
    else:
        aja_boonus=0
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
        font = pygame.font.SysFont("comicsansms",50)
        textSurface, textRect = text_objects("Pick your question", font)
        textRect.center = (250,100)
        screen.blit(textSurface, textRect)

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
        font = pygame.font.SysFont("comicsansms",20)
        display_text(screen,tekst,(20,20),font,white)
        pygame.draw.rect(screen, color, input_rect)
        text_surface=base_font.render(user_text,True,('black'))

        screen.blit(text_surface,(input_rect.x+5,input_rect.y-5))
    
        pygame.display.update()
        clock.tick(60)