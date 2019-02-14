<?php

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

}