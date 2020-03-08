class Game:
    def __init__(self, is_running):
        self.is_running = is_running

    def start_game(self):
        self.is_running = True

    def kill_screen(self, reason: str) -> None:
        self.is_running = False

