import pygame

pygame.init()

#Tamanho da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
LARGURA_CELULA = 32
ALTURA_CELULA = 32

#Mapa
LARGURA_MAPA = 30
ALTURA_MAPA = 30

#Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (100, 100, 100)

#Cores do jogo
COLOR_DEFAULT_BG = CINZA

#Sprites
S_PLAYER = pygame.image.load("data/almox.png")
S_ENEMY = pygame.image.load("data/goblin.png")
S_WALL = pygame.image.load("data/parede_placeholder.png")
S_FLOOR = pygame.image.load("data/chao_placeholder.png")