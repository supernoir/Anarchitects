<?php

class PlotController {
  const AVAILABLE_PLOTS = 100;
  const STARTING_PLOT = 1;

  public function createPlotMatrix ($plots)
  {
    $plotArr[] = [$plots];
  }

  public function hasRemainingPlots ($takenPlots)
  {
    $hasPlots = false;
    if ($takenPlots > AVAILABLE_PLOTS)
    {
      $hasPlots = true;
    }
    return $hasPlots;
  }

}