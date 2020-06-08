import pygame
import libtcod
#game files
import constants

def draw_game():

    global SURFACE_MAIN

    #clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    #TODO draw the map

    #draw the character
    SURFACE_MAIN.blit(constants.S_PLAYER, (200,200)) #(personagem, tupla onde o boneco se posiciona)

    #TODO update the display
    pygame.display.flip()


def game_main_loop():
    #função que faz o loop principal do jogo
    game_quit = False

    while not game_quit:

        #get player input
        events_list = pygame.event.get()

        #process imput
        for event in events_list:
            if event.type == pygame.QUIT:
                game_quit = True

        #draw the game
        draw_game()
    
    #quit the game
    pygame.quit()
    exit()

def game_initialize():
    #inicia a tela principal do jogo
    global SURFACE_MAIN
    #inicia pygame
    pygame.init()
    
    SURFACE_MAIN = pygame.display.set_mode( (constants.LARGURA_TELA, constants.ALTURA_TELA) )

if __name__ == '__main__':
    game_initialize()
    game_main_loop()
