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

class struc_Tile:
    def __init__(self, block_path):
        self.block_path = block_path
#se tile = False, o player pode caminhar sobre ele; é chão
#se tile = True, não pode caminhar; é parede

# _____ _     _           _       
#|  _  | |   (_)         | |      
#| | | | |__  _  ___  ___| |_ ___ 
#| | | | '_ \| |/ _ \/ __| __/ __|
#\ \_/ / |_) | |  __/ (__| |_\__ \
# \___/|_.__/| |\___|\___|\__|___/
#           _/ |                  
#          |__/      

class obj_Actor: 
    def __init__(self, x, y, name_object, sprite, creature = None): #cria o ator e seta as coordenadas dele
        self.x = x #endereço no mapa
        self.y = y #endereço no mapa
        self.sprite = sprite

        if creature:
            self.creature = creature
            creature.owner = self 


    def draw(self): #desenha o boneco na tela
        SURFACE_MAIN.blit(self.sprite, (self.x*constants.LARGURA_CELULA, self.y*constants.ALTURA_CELULA))
        
    def move(self, dx, dy): #move o ator
        #dx = distancia para mover x.  dy = distancia para mover y.
        #O ator checa aonde está e aonde vai.
        #vê se para onde ele quer ir é parede ou chão
        if GAME_MAP[self.x * dx][self.y * dy].block_path == False:
            self.x += dx
            self.y += dy

# _____                                              _       
#/  __ \                                            | |      
#| /  \/ ___  _ __ ___  _ __   ___  _ __   ___ _ __ | |_ ___ 
#| |    / _ \| '_ ` _ \| '_ \ / _ \| '_ \ / _ \ '_ \| __/ __|
#| \__/\ (_) | | | | | | |_) | (_) | | | |  __/ | | | |_\__ \
# \____/\___/|_| |_| |_| .__/ \___/|_| |_|\___|_| |_|\__|___/
#                      | |                                   
#                      |_|

class com_Creature:
    #tem hp, causa dano a outros objetos atacando eles
    def __init__(self, name_instance, hp = 10):
        self.name_instance = name_instance
        self.hp = hp
#class com_Items:

#class com_Container:

#___  ___            
#|  \/  |            
#| .  . | __ _ _ __  
#| |\/| |/ _` | '_ \ 
#| |  | | (_| | |_) |
#\_|  |_/\__,_| .__/ 
#             | |    
#             |_|

def map_create():
    new_map = [[struc_Tile(False) for y in range(0, constants.ALTURA_MAPA)] for x in range(0,constants.LARGURA_MAPA)] 
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

def draw_game():

    global SURFACE_MAIN

    #limpa a surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    #desenha o mapa
    draw_map(GAME_MAP)

    #desenha o personagem na tela na ordem listada
    ENEMY.draw()
    PLAYER.draw()
    
    #atualiza a tela
    pygame.display.flip()

def draw_map(map_to_draw):

    for x in range (0, constants.LARGURA_MAPA):
        for y in range (0, constants.ALTURA_MAPA):
            if map_to_draw[x][y].block_path == True: #se verdade, desenhar uma parede aqui
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

        #pega o input do jogador
        events_list = pygame.event.get()

        #processa o input
        for event in events_list: #faz o loop de todos os eventos que aconteceram
            if event.type == pygame.QUIT: # atributo QUIT detecta que alguém fechou a janela do jogo
                game_quit = True

            if event.type == pygame.KEYDOWN: #detecta a pressão das teclas no teclado
                if event.key == pygame.K_UP:
                    PLAYER.move(0, -1)
                if event.key == pygame.K_DOWN:
                    PLAYER.move(0, 1)
                if event.key == pygame.K_LEFT:
                    PLAYER.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    PLAYER.move(1, 0)

        #draw the game
        draw_game()
    
    #quit the game
    pygame.quit()
    exit()


def game_initialize():
    #inicia a tela principal do jogo
    global SURFACE_MAIN, GAME_MAP, PLAYER, ENEMY
    #inicia pygame
    pygame.init()
    
    SURFACE_MAIN = pygame.display.set_mode( (constants.LARGURA_TELA, constants.ALTURA_TELA) )

    GAME_MAP = map_create() # guarda o mapa criado na função do mapa nesta variável
    # preenche a matriz com valores

    creature_com1 = com_Creature ("almox")
    PLAYER = obj_Actor(0, 0, "human", constants.S_PLAYER, creature = creature_com)

    creature_com2 = com_Creature ("eggshell")
    ENEMY = obj_Actor(15, 15, "goblin", constants.S_ENEMY)

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
