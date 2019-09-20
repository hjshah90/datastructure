<?php

$input = array(14, 33, 27, 35, 10);
echo "Unsorted Array :: \n";
echo implode(', ', $input)."\n\n";
echo "Start Sorting :: \n\n";

$size = count($input);
$step = 0;


for($i = 0; $i < $size; $i++) {
  for($j = $i+1; $j < $size; $j++) {
    $step++;
    $min = $input[$i];
    if($input[$j] < $min) {
      $min = $input[$j];
      $minkey = $j;
    }
    if($min != $input[$i]) {
      $temp = $input[$i];
      $input[$i] = $min;
      $input[$minkey] = $temp;
    }
    echo "Step :: ".$step."\n";
    echo implode(', ', $input)."\n";
  }
}

