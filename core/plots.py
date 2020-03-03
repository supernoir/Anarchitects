class Plot:
    availablePlots = 100
    startingPlot = 1

    def __init__(self, takenplots, availableplots):
        self.takenPlots = takenplots
        self.availablePlots = availableplots

    def hasremainingplots(self, takenPlots, availablePlots):
        hasPlots = False
        if (takenPlots > availablePlots):
            hasPlots = True
        return hasPlots