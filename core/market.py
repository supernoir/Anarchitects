import json


class Market:
    def __init__(self, players):
        self.players = players

    def get_competitors(self) -> object:
        return json.dumps(self.players)
