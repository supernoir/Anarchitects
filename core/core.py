initialBalance = 100
initialPlotPrice = 25
initialPlotCount = 1

playerBalance = initialBalance
playerPlots = initialPlotCount
plotPrice = initialPlotPrice
playerName = "Player1"

totalPlots = 1000


def getPlayerName(name: str):
    print(f'Player name: {name}')


def canBuyPlot(balance: float) -> bool:
    if balance < initialPlotPrice and playerPlots < totalPlots - 1:
        return False
    else:
        return True


def startGame():
    getPlayerStatus()


def getPlayerStatus():
    print(
        f'{playerName} has {playerPlots}/{totalPlots} plots and an account balance of {playerBalance}'
    )


def sendUserMessage(message):
    print(f'{message}')


# actions
def purchasePlot(balance: float, plots: int):
    global playerBalance
    global playerPlots
    global totalPlots
    if (canBuyPlot(balance)):
        balance - plotPrice
        playerBalance = balance
        plots + 1
        totalPlots - 1
        playerPlots = plots
        print(balance, plots, totalPlots)
        sendUserMessage("Plot purchase successful")
    else:
        sendUserMessage("Plot purchase failed. Insufficient funds")


startGame()
purchasePlot(playerBalance, playerPlots)
print(playerBalance)
getPlayerStatus()
