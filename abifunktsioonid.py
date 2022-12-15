#tagastab tekstipinna ja sellest ristküliku ekraanile kuvamiseks
from värvid import*
import pygame
pygame.init()
pygame.font.init()

import random
def valik(n):
    valik1=random.randint(1,n)
    valik2=random.randint(1,n)
    while valik1==valik2:
        valik2=random.randint(1,n)
    valik3=random.randint(1,n)
    while valik3==valik2 or valik3==valik1:
        valik3=random.randint(1,n)
    return valik1, valik2, valik3

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    textRect = textSurface.get_rect()
    return textSurface, textRect

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

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def info():
    järjend=[]
    sõnastik={}
    with open ("küsimused_ja_vastused.txt",encoding="UTF-8") as f:
        for rida in f:
            rida=rida.strip().split(";")
            järjend.append(rida[0])
            sõnastik[rida[0]]=rida[1]
        return järjend, sõnastik