#tagastab tekstipinna ja sellest ristküliku ekraanile kuvamiseks
from värvid import*
import pygame
pygame.init()
pygame.font.init()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
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