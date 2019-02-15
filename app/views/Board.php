<?php

include './messages/Message.php';
use Messenger;

class Board {
  
  public function renderBoard()
  {
    $element = NULL;
    $elementName = 'Board';

    $element .= '<div class="col-8">';
      $element .= '<div class="card">';
        $element .= '<h3 class="card-header">'. $elementName  .'</h3>';
        $element .= '<div class="card-body">';
          $element .= '<ul>';
            $element .= '<li>' . self::projectPlots(99,100) . '</li>';
          $element .= '</ul>';
          $element .= '<hr/>';
          $element .= '<a href="#" class="btn btn-primary">Next Turn</a>';

        $element .= '</div>';
      $element .= '</div>';
    $element .= '</div>';
    
    if(isset($element)){
      echo $element;
    } else {
      echo Messenger\Message::render('error','Could not load ' . $elementName);
    }
  }

  protected function projectPlots($maxPlots, $totalPlots)
  {
    $availablePlots = 'There are ' . $maxPlots . '/' . $totalPlots . ' plots to build on';
    return $availablePlots;
  }

}