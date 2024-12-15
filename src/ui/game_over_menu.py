import pygame

from src.constants import FONT_SIZE
from src.objects.player import Player


class GameOverMenu:
    def __init__(self, screen: pygame.display, player: Player) -> None:
        self.screen: pygame.display = screen
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.large_font = pygame.font.Font(None, FONT_SIZE * 2)
        self.player: Player = player
        self.exit_button_rect = pygame.Rect(
            self.screen.get_width() // 2 - 100,
            self.screen.get_height() // 2 + 100,
            200,
            50,
        )

    def draw(self) -> None:
        self.screen.fill("black")

        game_over_text = self.large_font.render("GAME OVER", True, "red")
        text_rect = game_over_text.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 100)
        )
        self.screen.blit(game_over_text, text_rect)

        final_score_text = self.font.render(
            f"Final Score: {self.player.score}", True, "white"
        )
        score_rect = final_score_text.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
        )
        self.screen.blit(final_score_text, score_rect)

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
                    if self.exit_button_rect.collidepoint(event.pos):
                        return

            self.draw()
