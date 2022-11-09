import time
import pygame
import os
pygame.init()

pygame.display.set_caption("projekt")
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

#värvid
white=(255,255,255)
black=(0,0,0)
lightblue= (173,216,230)
darkblue = (104,131,139)


#tagastab tekstipinna ja sellest ristküliku ekraanile kuvamiseks
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    textRect = textSurface.get_rect()
    return textSurface, textRect

#neid valikuid saame kasutada küsimuste valimisel
import random
def valik():
    valik1=random.randint(1,3)
    valik2=random.randint(1,3)
    while valik1==valik2:
        valik2=random.randint(1,3)
    valik3=random.randint(1,3)
    while valik3==valik2 or valik3==valik1:
        valik3=random.randint(1,3)
    return valik1, valik2, valik3

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

        valik()
        button("1",185,310,120,15,"valik1")
        button("2", 185,330,120,15,"valik2")
        button("3", 185,350,120,15,"valik3")
        pygame.display.update()
        clock.tick(15)

# nupu funktsioon, peab täiendama, et ei kontrolliks vaid esimese vajutuse commande, vaid hoopis tagastaks commandi et funktsiooni saaks kasutada läbi terve programmi
def button(word,x,y,width,height,command):
    mouse =  pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #X-koordinaat + laius, Y-koordinaat + kõrgus
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(screen, darkblue,(x,y,width,height))
       
        if click[0] == 1:
            if command == "sisene":
                gameloop()
            if command == "lõpeta":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen,lightblue,(x,y,width,height))

    text = pygame.font.Font(None,30)
    textSurface, textRect = text_objects(word, text)
    textRect.center = ( x+width/2, y+height/2) 
    screen.blit(textSurface, textRect)

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
    
       
        button("Alusta!",185,310,120,50,"sisene")
        button("Lõpeta", 185,390,120,50,"lõpeta")
    

        pygame.display.update()
        clock.tick(15)
intro()
