def displayTurn(turnCount, currentTurn):
    print(f'You are on turn {currentTurn} of {turnCount} so far.')

def displayCompetitors(players):
    print (", ".join(player for player in players))

def displayRemainingPlots(plotCount):
    # hasRemainingPlots = PlotController.hasRemainingPlots(plotCount)
    hasRemainingPlots = True
    if (hasRemainingPlots):
        remainingPlots = "There are {plotCount} plots remaining".format(plotCount)
    else:
        remainingPlots = 'There are no remaining plots to build on'
    return remainingPlots