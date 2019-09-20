<?php

$input = array(14, 33, 27, 35, 10);
echo "Unsorted Array :: \n";
echo implode(', ', $input)."\n\n";
echo "Start Sorting :: \n\n";

$size = count($input);
$step = 0;


for($i = 1; $i < $size; $i++) {
  for($j = $i; $j > 0; $j--) {
    $step++;
    if($input[$j] < $input[$j-1]) {
      $temp = $input[$j];
      $input[$j] = $input[$j-1];
      $input[$j-1] = $temp;
    }
    echo "Step :: ".$step."\n";
    echo implode(', ', $input)."\n";
  }
}

