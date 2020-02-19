class PlotController:
    availablePlots = 100
    startingPlot = 1

    def hasRemainingPlots(self, takenPlots, availablePlots):
        hasPlots = False
        if (takenPlots > availablePlots):
            hasPlots = True
        return hasPlots
