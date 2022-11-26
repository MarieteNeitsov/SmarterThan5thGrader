import pygame
import sys
from tekstipind import*
 
screen = pygame.display.set_mode([500, 500])

def nupufunktsioon(sõnum,Xtelg,Ytelg,laius,kõrgus,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    print(click)

    if Xtelg+laius>mouse[0]>Xtelg and Ytelg+kõrgus>mouse[1]>Ytelg:
        pygame.draw.rect(screen, ac,(Xtelg,Ytelg,laius,kõrgus))
        
        if click[0]==1 and action!=None:
            action()
    else:

        pygame.draw.rect(screen, ic,(Xtelg,Ytelg,laius,kõrgus))
    
    pygame.init()
    väiketekst=pygame.font.SysFont("comicsansms",20)
    textSurf,textRect=text_objects(sõnum,väiketekst)
    textRect.center=((Xtelg+laius/2),(Ytelg+kõrgus/2))
    screen.blit(textSurf,textRect)