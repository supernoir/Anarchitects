<?php

class Board {

  public function renderBoard()
  {
    echo '<div class="col-8">';
      echo '<div class="card">';
        echo '<h3 class="card-header">'. 'Board'  .'</h3>';
        echo '<div class="card-body">';
          echo '<ul>';
            echo '<li>' . self::projectPlots(99,100) . '</li>';
          echo '</ul>';
          echo '<hr/>';
          echo '<a href="#" class="btn btn-primary">Next Turn</a>';

        echo '</div>';
      echo '</div>';
    echo '</div>';
  }

  protected function projectPlots($maxPlots, $totalPlots)
  {
    $availablePlots = 'There are ' . $maxPlots . '/' . $totalPlots . ' plots to build on';
    return $availablePlots;
  }

}