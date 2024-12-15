import pygame
from src.constants import (
    PAUSE_MENU_PANEL_WIDTH,
    PAUSE_MENU_PANEL_HEIGHT,
    PAUSE_MENU_BUTTON_WIDTH_OFFSET,
    PAUSE_MENU_BUTTON_HEIGHT,
    PAUSE_MENU_BUTTON_LEFT_OFFSET,
    PAUSE_MENU_BUTTON_TOP_BASE_OFFSET,
    PAUSE_MENU_BUTTON_TOP_CONSECUTIVE_OFFSET,
    FONT_STYLE_PATH,
    FONT_SIZE,
)


class PauseMenu:
    def __init__(self, screen: pygame.Surface):
        self.screen: pygame.Surface = screen
        self.menu_panel: pygame.Rect = pygame.Rect(
            (self.screen.get_width() - PAUSE_MENU_PANEL_WIDTH) // 2,
            (self.screen.get_height() - PAUSE_MENU_PANEL_HEIGHT) // 2,
            PAUSE_MENU_PANEL_WIDTH,
            PAUSE_MENU_PANEL_HEIGHT,
        )
        self.is_visible: bool = False

        self.button_width = PAUSE_MENU_PANEL_WIDTH - PAUSE_MENU_BUTTON_WIDTH_OFFSET
        self.button_height = PAUSE_MENU_BUTTON_HEIGHT
        self.resume_button: pygame.Rect = pygame.Rect(
            self.menu_panel.left + PAUSE_MENU_BUTTON_LEFT_OFFSET,
            self.menu_panel.top + PAUSE_MENU_BUTTON_TOP_BASE_OFFSET,
            self.button_width,
            self.button_height,
        )
        self.exit_button: pygame.Rect = pygame.Rect(
            self.menu_panel.left + PAUSE_MENU_BUTTON_LEFT_OFFSET,
            self.menu_panel.top
            + PAUSE_MENU_BUTTON_TOP_BASE_OFFSET
            + PAUSE_MENU_BUTTON_TOP_CONSECUTIVE_OFFSET,
            self.button_width,
            self.button_height,
        )

    def draw(self) -> None:
        pygame.draw.rect(self.screen, "black", self.menu_panel)
        pygame.draw.rect(self.screen, "white", self.menu_panel, width=2)

        pygame.draw.rect(self.screen, "white", self.resume_button)
        pygame.draw.rect(self.screen, "white", self.exit_button)

        font = pygame.font.Font(FONT_STYLE_PATH, FONT_SIZE)
        resume_text = font.render("Resume", True, "black")
        exit_text = font.render("Exit", True, "black")

        resume_text_rect = resume_text.get_rect(center=self.resume_button.center)
        exit_text_rect = exit_text.get_rect(center=self.exit_button.center)

        self.screen.blit(resume_text, resume_text_rect)
        self.screen.blit(exit_text, exit_text_rect)

    def show(self) -> None:
        self.is_visible = True
        self.loop()

    def loop(self) -> None:
        while self.is_visible:
            self.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_visible = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.resume_button.collidepoint(event.pos):
                        self.is_visible = False
                        return

                    if self.exit_button.collidepoint(event.pos):
                        self.is_visible = False
                        pygame.quit()
                        return
