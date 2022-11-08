import time
import pygame
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

# nupu funktsioon
def button(word,x,y,width,height,command):
    mouse =  pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #X-koordinaat + laius, Y-koordinaat + kõrgus
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(screen, darkblue,(x,y,width,height))
       
        if click[0] == 1:
            if command == "sisene":
                game_loop()
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
def game_loop():
    

intro()
