class Turn:

    def __init__(self, total_turns, current_turn):
        self.total_turns = total_turns
        self.current_turn = current_turn

    def next_turn(self):
        self.current_turn = self.current_turn + 1
        return self.current_turn

    def kill_screen(self, reason: str) -> object:
        return self.kill_screen(reason)

    def end_turn(self) -> bool:
        if self.current_turn < self.total_turns:
            print(f"Turn {self.current_turn} ended")
            self.current_turn = self.current_turn + 1
            return True
        else:
            self.kill_screen("You ran out of time")
            return False

    def display_turn(self) -> None:
        print(f'You are on turn {self.current_turn} of {self.total_turns - self.current_turn} so far.')