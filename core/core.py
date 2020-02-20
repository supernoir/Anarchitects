# CONSTANTS
initialBalance = 100
initialPlotPrice = 25
initialPlotCount = 1

# GLOBALS
playerName = "Player1"
playerBalance = initialBalance
playerPlots = initialPlotCount
plotPrice = initialPlotPrice
totalPlots = 1000
currentTurn = 1

# WIN STATES
maxTurns = 1000

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
    global playerName
    global playerPlots
    global totalPlots
    global playerBalance
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
        print(playerBalance, playerPlots, totalPlots)
        sendUserMessage("Plot purchase successful")
    else:
        sendUserMessage("Plot purchase failed. Insufficient funds")

def endTurn(turn):
    global maxTurns
    global currentTurn
    turn = currentTurn
    if turn < maxTurns:
        turn + 1
        getPlayerStatus()
        print(f"Turn {turn} ended")
    else:
        killScreen("You ran out of time")

def killScreen(reason):
    print(f"Game Over! {reason}")

startGame()
purchasePlot(playerBalance, playerPlots)
print(playerBalance)
getPlayerStatus()
endTurn(currentTurn)
purchasePlot(playerBalance, playerPlots)
endTurn(currentTurn)