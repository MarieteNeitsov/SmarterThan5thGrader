import time
import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()


white=(255,255,255)
black=(0,0,0)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def intro():
    intro = True
    while intro:
         for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        largeText = pygame.font.Font(None,100)
        TextSurf, TextRect = text_objects("Pealkiri", largeText)
        TextRect.center = ((500/2),(500/2))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)

def game_loop():
