import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)

ENTITY_SPEED = {
    'level1bg0': 0,
    'level1bg1': 1,
    'level1bg2': 2,
    'level1bg3': 3,
    'level1bg4': 4,
    'level1bg5': 5,
    'level1bg6': 6,
    'Player1': 3,
    'Player1Shot': 2,
    'Player2': 3,
    'Player2Shot': 2,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 3
}

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_HEALTH = {
    'level1bg0': 999,
    'level1bg1': 999,
    'level1bg2': 999,
    'level1bg3': 999,
    'level1bg4': 999,
    'level1bg5': 999,
    'level1bg6': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 50,
    'Enemy2Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 15,
    'Player2': 15,
    'Enemy1': 50,
    'Enemy2': 100
}

MENU_OPTIONS = (
    'NEW GAME 1P',
    'NEW GAME 2P - COOPERATIVE',
    'NEW GAME 2P - COMPETITIVE',
    'SCORE',
    'EXIT'
)

PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

SPAWN_TIME = 2000

WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324