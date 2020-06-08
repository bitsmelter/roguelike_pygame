import pygame
import libtcod
#game files
import constants


# _____ _                   _                  
#/  ___| |                 | |                 
#\ `--.| |_ _ __ _   _  ___| |_ _   _ _ __ ___ 
# `--. \ __| '__| | | |/ __| __| | | | '__/ _ \
#/\__/ / |_| |  | |_| | (__| |_| |_| | | |  __/
#\____/ \__|_|   \__,_|\___|\__|\__,_|_|  \___|

class struc_tile:
    def __init__(self, block_path):
        self.block_path = block_path
#se tile = False, o player pode caminhar sobre ele; é chão
#se tile = True, não pode caminhar; é parede

#___  ___            
#|  \/  |            
#| .  . | __ _ _ __  
#| |\/| |/ _` | '_ \ 
#| |  | | (_| | |_) |
#\_|  |_/\__,_| .__/ 
#             | |    
#             |_|

def map_create():
    new_map = [[struc_tile(False) for y in range(0, constants.ALTURA_MAPA)] for x in range(0,constants.LARGURA_MAPA)] 
    #mapa apenas com espaços vaios para teste

    new_map [10][10].block_path = True
    new_map [10][15].block_path = True

    return new_map

#______                    _             
#|  _  \                  (_)               ASCI WEBSITE:
#| | | |_ __ __ ___      ___ _ __   __ _    http://www.patorjk.com/software/taag/#p=display&f=Doom&t=
#| | | | '__/ _` \ \ /\ / / | '_ \ / _` |   
#| |/ /| | | (_| |\ V  V /| | | | | (_| |
#|___/ |_|  \__,_| \_/\_/ |_|_| |_|\__, |
#                                   __/ |
#                                  |___/ 

#DEFINITIONS

def draw_game():

    global SURFACE_MAIN

    #clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    #draw the map
    draw_map(GAME_MAP)

    #draw the character
    SURFACE_MAIN.blit(constants.S_PLAYER, (200,200)) #(personagem, tupla onde o boneco se posiciona)

    #TODO update the display
    pygame.display.flip()

def draw_map(map_to_draw):

    for x in range (0,30):
        for y in range (0,30):
            if map_to_draw[x][y].block_path == True:
                #desenha a parede
                SURFACE_MAIN.blit(constants.S_WALL, (x*constants.LARGURA_CELULA, y*constants.ALTURA_CELULA))
            else:
                #desenha o chão
                SURFACE_MAIN.blit(constants.S_FLOOR, (x*constants.LARGURA_CELULA, y*constants.ALTURA_CELULA))

# _____                      
#|  __ \                     
#| |  \/ __ _ _ __ ___   ___ 
#| | __ / _` | '_ ` _ \ / _ \
#| |_\ \ (_| | | | | | |  __/
# \____/\__,_|_| |_| |_|\___|

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
    global SURFACE_MAIN, GAME_MAP
    #inicia pygame
    pygame.init()
    
    SURFACE_MAIN = pygame.display.set_mode( (constants.LARGURA_TELA, constants.ALTURA_TELA) )

    GAME_MAP = map_create() # guarda o mapa criado na função do mapa nesta variável

'''
                       .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ##                 ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!
          `..::!8888888888888888888888888888888899fT|!^"'
            `' !!988888888888888888888888899fT|!^"'
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'
'''

if __name__ == '__main__':
    game_initialize()
    game_main_loop()
