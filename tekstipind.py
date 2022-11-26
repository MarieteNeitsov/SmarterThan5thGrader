#tagastab tekstipinna ja sellest ristküliku ekraanile kuvamiseks
from värvid import*
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    textRect = textSurface.get_rect()
    return textSurface, textRect