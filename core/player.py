class Player:

    def __init__(self, name: str, plots: int, balance: float):
        self.name = name,
        self.plots = plots,
        self.balance = balance

    def get_player_name(self):
        return self.name

    def get_player_status(self):
        return {
            "player": {
                "name": self.name,
                "plots": self.plots,
                "balance": self.balance
            }
        }