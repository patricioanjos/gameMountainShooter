import pygame

ENTITY_SPEED = {
    'level1bg0': 0,
    'level1bg1': 1,
    'level1bg2': 2,
    'level1bg3': 3,
    'level1bg4': 4,
    'level1bg5': 5,
    'level1bg6': 6,
    'Player1': 3,
    'Player2': 3,
}

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)

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

WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324