import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_ORANGE, MENU_OPTIONS, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(50, True, "Mountain", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 70))
            self.menu_text(50, True, "Shooter", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 120))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(20, False, MENU_OPTIONS[i], COLOR_ORANGE, ((WINDOW_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, False, MENU_OPTIONS[i], COLOR_WHITE, ((WINDOW_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            #Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting...")
                    pygame.quit()  # Close window
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1

                    if event.key == pygame.K_RETURN: #Tecla ENTER
                        return MENU_OPTIONS[menu_option]


    def menu_text(self, text_size: int, text_bold: bool, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont('comicsans', size=text_size, bold=text_bold)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)

        self.window.blit(source=text_surface, dest=text_rect)