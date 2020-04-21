import pygame, sys
from pygame import mixer
# Setup Window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Mario Bar Game')
screen = pygame.display.set_mode((800, 600),0,32)
 
font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:
        # Background
        screen.fill((0,0,0))

        # Text on Main Menu
        plyr1Font = pygame.font.Font('freesansbold.ttf', 30)
        plyr1Text = plyr1Font.render('1 PLAYER GAME', True, (225, 225, 255))
        plyr2Font = pygame.font.Font('freesansbold.ttf', 30)
        plyr2Text = plyr2Font.render('2 PLAYER GAME', True, (225, 225, 255))

        
        plyr1Button = screen.blit(plyr1Text, (275, 300))
        plyr2Button = screen.blit(plyr2Text, (275, 375)) 
        
        mouseX, mouseY = pygame.mouse.get_pos()

        if plyr1Button.collidepoint((mouseX, mouseY)):
            if click:
                
                game()
        if plyr2Button.collidepoint((mouseX, mouseY)):
            if click:
                
                quitMenu()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text("Game", font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)


def quitMenu():
    pygame.quit()
    sys.exit()


main_menu()