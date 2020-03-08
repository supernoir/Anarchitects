from turns import Turn
from plots import Plot
from player import Player

# CONSTANTS
initial_balance = 100
initial_plot_price = 25
initial_plot_amt = 50
initial_player_plots = 1

# GLOBALS
player_name = "PrincessBubblegum"
player_balance = initial_balance
player_plots = initial_player_plots
plot_price = initial_plot_price
current_turn = 1

# WIN STATES
max_turns = 1000

# Fake Players for testing
players = ["Mr. Robot", "Selena Kyle", "ReadyPlayer1", player_name]

# Testing TURN
game_turns = Turn(max_turns, current_turn)

current_turn = game_turns.next_turn()
game_turns.display_turn()
current_turn = game_turns.next_turn()
game_turns.display_turn()


# Testing PLOT
new_player_plot = Plot(100, 10, 2929.43, 1050.50)

new_player_plot.purchase_plot()
new_player_plot.purchase_plot()
new_player_plot.purchase_plot()

# Testing PLAYER

new_player = Player(player_name, player_plots, player_balance)
print(new_player.get_player_name())
print(new_player.get_player_status())