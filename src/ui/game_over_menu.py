import pygame

from src.constants import (
    FONT_SIZE,
    FONT_STYLE_PATH,
    GAME_OVER_TEXT_CENTER_HEIGHT_OFFSET,
    GAME_OVER_FINAL_SCORE_CENTER_HEIGHT_OFFSET,
    GAME_OVER_BUTTON_CENTER_LEFT_OFFSET,
    GAME_OVER_BUTTON_CENTER_HEIGHT_OFFSET,
    GAME_OVER_BUTTON_WIDTH,
    GAME_OVER_BUTTON_HEIGHT,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_PATH,
)
from src.objects.player import Player


class GameOverMenu:
    def __init__(
        self, screen: pygame.display, player: Player, restart: callable
    ) -> None:
        self.screen: pygame.display = screen
        self.background = pygame.image.load(BACKGROUND_PATH)
        self.background = pygame.transform.scale(
            self.background, (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.font = pygame.font.Font(FONT_STYLE_PATH, FONT_SIZE)
        self.large_font = pygame.font.Font(FONT_STYLE_PATH, FONT_SIZE * 2)
        self.player: Player = player
        self.restart_button_rect: pygame.Rect = pygame.Rect(
            self.screen.get_width() // 2 + GAME_OVER_BUTTON_CENTER_LEFT_OFFSET,
            self.screen.get_height() // 2 + GAME_OVER_BUTTON_CENTER_HEIGHT_OFFSET,
            GAME_OVER_BUTTON_WIDTH,
            GAME_OVER_BUTTON_HEIGHT,
        )
        self.exit_button_rect: pygame.Rect = pygame.Rect(
            self.screen.get_width() // 2 + GAME_OVER_BUTTON_CENTER_LEFT_OFFSET,
            self.screen.get_height() // 2
            + GAME_OVER_BUTTON_CENTER_HEIGHT_OFFSET * 1.5
            + GAME_OVER_BUTTON_HEIGHT,
            GAME_OVER_BUTTON_WIDTH,
            GAME_OVER_BUTTON_HEIGHT,
        )
        self.restart = restart

    def draw(self) -> None:
        self.screen.blit(self.background, (0, 0))

        game_over_text = self.large_font.render("GAME OVER", True, "red")
        text_rect = game_over_text.get_rect(
            center=(
                self.screen.get_width() // 2,
                self.screen.get_height() // 2 + GAME_OVER_TEXT_CENTER_HEIGHT_OFFSET,
            )
        )
        self.screen.blit(game_over_text, text_rect)

        final_score_text = self.font.render(
            f"Final Score: {self.player.score}", True, "white"
        )
        score_rect = final_score_text.get_rect(
            center=(
                self.screen.get_width() // 2,
                self.screen.get_height() // 2
                + GAME_OVER_FINAL_SCORE_CENTER_HEIGHT_OFFSET,
            )
        )
        self.screen.blit(final_score_text, score_rect)

        pygame.draw.rect(self.screen, "white", self.restart_button_rect)
        restart_text = self.font.render("Restart", True, "black")
        restart_text_rect = restart_text.get_rect(
            center=self.restart_button_rect.center
        )
        self.screen.blit(restart_text, restart_text_rect)

        pygame.draw.rect(self.screen, "white", self.exit_button_rect)
        exit_text = self.font.render("Exit", True, "black")
        exit_text_rect = exit_text.get_rect(center=self.exit_button_rect.center)
        self.screen.blit(exit_text, exit_text_rect)

        pygame.display.flip()

    def loop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.restart_button_rect.collidepoint(event.pos):
                        self.restart()
                        return

                    if self.exit_button_rect.collidepoint(event.pos):
                        return

            self.draw()
