class Plot:
    availablePlots = 100
    startingPlot = 1

    def __init__(self,
                 total_plots: int,
                 player_plots: int,
                 player_balance: float,
                 plot_price: float
                 ):
        self.total_plots = total_plots
        self.player_plots = player_plots
        self.player_balance = player_balance
        self.plot_price = plot_price

    def can_buy_plot(self, balance: float) -> bool:
        if balance < self.plot_price and self.player_plots < self.total_plots - 1:
            return False
        else:
            return True

    def purchase_plot(self) -> bool:
        if self.can_buy_plot(self.player_balance):
            self.player_balance = self.player_balance - self.plot_price
            self.player_plots += 1
            self.total_plots -= 1
            print(self.player_balance, self.player_plots, self.total_plots)
            print("Plot purchase successful")
            return True
        else:
            print("Plot purchase failed. Insufficient funds")
            return False

    def has_remaining_plots(self) -> bool:
        has_plots = False
        if self.player_plots > self.total_plots:
            has_plots = True
        return has_plots
