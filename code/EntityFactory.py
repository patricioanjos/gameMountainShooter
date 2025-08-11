import random

from code.Background import Background
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name.lower():
            case 'level1bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'player1':
                return Player('Player1', (10, WINDOW_HEIGHT / 2 - 30))
            case 'player2':
                return Player('Player2', (10, WINDOW_HEIGHT / 2 + 30))
            case 'enemy1':
                return Enemy('Enemy1', (WINDOW_WIDTH + 10, random.randint(0, WINDOW_HEIGHT)))
            case 'enemy2':
                return Enemy('Enemy2', (WINDOW_WIDTH + 10, random.randint(0, WINDOW_HEIGHT)))
        return None