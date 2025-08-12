import random
import sys

import pygame
from pygame import Surface
from pygame.font import Font

from code.Const import COLOR_WHITE, WINDOW_HEIGHT, MENU_OPTIONS, EVENT_ENEMY, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))
        self.entity_list.append(EntityFactory.get_entity('player1'))

        if game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(EntityFactory.get_entity('player2'))

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

        self.timeout = 20000

    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps()}', COLOR_WHITE, (10, WINDOW_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WINDOW_HEIGHT - 20))
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, tex_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface: Surface = text_font.render(text, True, tex_color).convert_alpha()
        text_rect = text_surface.get_rect(left=text_position[0], top=text_position[1])
        self.window.blit(source=text_surface, dest=text_rect)