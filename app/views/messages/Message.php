<?php
namespace Messenger;

class Message {
  
  public function render($type, $message)
  {
    $errorElement = NULL;
    switch($type){
      case 'default':
        $errorElement = self::deriveFromTemplate('alert-primary', $message);
        break;
      case 'error':
        $errorElement = self::deriveFromTemplate('alert-danger', $message);
        break;
    }
    return $errorElement;
  }

  private function deriveFromTemplate($template, $message)
  {
  $errorTemplate = NULL;

  $errorTemplate .= '<div class="alert ' . $template .'" role="alert">';
    $errorTemplate .= $message;
  $errorTemplate .= '</div>';

  return $errorTemplate;
  }

}