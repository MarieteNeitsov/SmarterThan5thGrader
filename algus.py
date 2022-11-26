from tekstipind import*
import pygame

screen = pygame.display.set_mode([500, 500])

def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
        screen.fill(white)
        font = pygame.font.Font(None,100)
        textSurface, textRect = text_objects("Pealkiri", font)
        textRect.center = (500/2,500/2)
        screen.blit(textSurface, textRect)
    
       
        nupufunktsioon("Alusta",250, 100,75,20,darkblue, lightblue,gameloop)
        nupufunktsioon("Lõpeta", 350,100,75,20,darkblue,lightblue,pygame.quit)
    

        pygame.display.update()
        clock.tick(15)