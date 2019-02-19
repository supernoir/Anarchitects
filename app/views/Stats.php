<?php

require('../controllers/PlotController.php');

class Stats {

  public function renderStats()
  {
    echo '<div class="col-4">';
      echo '<div class="card">';
        echo '<h3 class="card-header">'. 'Stats'  .'</h3>';
        echo '<div class="card-body">';
          echo '<ul>';
            echo '<li>' . self::displayTurn(132,1) . '</li>';
            echo '<li>' . self::displayCompetitors(['Julie Chao','Caracasa','Bernadette']) . '</li>';
            echo '<li>' . self::displayRemainingPlots(12) . '</li>';
          echo '</ul>';
        echo '</div>';
      echo '</div>';
    echo '</div>';
  }

  protected function displayTurn($turnCount, $currentTurn)
  {
    $turnOfTurns = 'You are on turn ' . $currentTurn . ' of ' . $turnCount .' so far.';
    return $turnOfTurns;
  }

    protected function displayCompetitors($players)
  {
    $turnOfTurns = 'Players <b>' . implode(', ',$players) .'</b> are still in the game with you.';
    return $turnOfTurns;
  }

  protected function displayRemainingPlots($plots)
  {
    $hasRemainingPlots = PlotController::hasRemainingPlots($plots);
    if ($hasRemainingPlots)
    {
      $remainingPlots = 'There are ' . $plots . ' plots remaining.';
    } else {
      $remainingPlots = 'There are no remaining plots to build on';
    }
    return $remainingPlots;
  }

}