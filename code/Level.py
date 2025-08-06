import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))

    def run(self):
        while True:
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
            pygame.display.flip()
        pass