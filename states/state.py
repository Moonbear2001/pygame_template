from pygame.locals import QUIT
import pygame


class State:

    def __init__(self, game):
        self.name = ""
        self.game = game
        self.prev_state = None

    def update(self):
        pass

    def render(self):

        # Print game info
        fps = f"FPS: {self.game.fps}"
        self.game.render_text(self.game.canvas, fps, "roboto", self.game.colors["blue"],
                              0.01 * self.game.canvas_width, 0.03 * self.game.canvas_height, size=20, center=False)
        stack = "State stack: "
        for state in self.game.state_stack:
            stack += state.name + ", "
        self.game.render_text(self.game.canvas, stack, "roboto", self.game.colors["blue"],
                              0.01 * self.game.canvas_width, 0.08 * self.game.canvas_height, size=20, center=False)

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        else:
            self.prev_state = None
        self.game.state_stack.append(self)

    def handle_event(self, event):

        if event.type == pygame.QUIT:
            self.exit_state()
            self.game.game_quit()

        # Press T to return to title screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                self.exit_state()
            if event.key == pygame.K_ESCAPE:
                self.exit_state()
                self.game.game_quit()

    def exit_state(self):
        self.game.state_stack.pop()
