import pygame

from .scene import Scene
from utilities import render_text
from managers import SaveLoadManager


class Clicker(Scene):
    """
    Simple clicker game in which the player just tries to beat the high score number of
    clicks.
    """

    name = "clicker"
    custom_watched_events = {pygame.MOUSEBUTTONDOWN}

    def __init__(self):
        super().__init__(watched_events=self.custom_watched_events)
        self.score = 0
        self.saved_data = SaveLoadManager().load_data("clicker")
        self.high_score = self.saved_data["high_score"]

    def _render_before_children(self):
        self.canvas.fill("gray")
        render_text(
            self.canvas,
            "The high score is: " + str(self.high_score),
            "roboto",
            "blue",
            coord=(self.rect.width / 2, self.rect.height * 0.9),
            size=30,
        )
        render_text(
            self.canvas,
            str(self.score),
            "roboto",
            "black",
            coord=(self.rect.width / 2, self.rect.height / 2),
            size=60,
        )
        return self.canvas

    def _on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.score += 1

    def _on_enter(self):
        pass

    def _on_leave(self):
        """
        Save new high score if acheived before exiting.
        """
        self.high_score = max(self.high_score, self.score)
        self.saved_data["high_score"] = self.high_score
        SaveLoadManager().save_data(self.saved_data, "clicker")
