<?php

class PlotController extends GameController {
  const AVAILABLE_PLOTS = 100;
  const STARTING_PLOT = 1;

  public function createPlotMatrix ($plots)
  {
    $plotArr[] = [$plots];
  }

}