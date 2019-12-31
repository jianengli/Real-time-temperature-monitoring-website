<?php

    $file = fopen("./TempInfo.txt", 'a')or die("Unable to open file!");;
        
    $date = $_GET["date"];
    $time = $_GET["time"];
    $temperature = $_GET["temperature"];
        
    fputs($file, ($date.",".$time.",".$temperature).PHP_EOL);
    
    $arrayJSON[] = array("date"=>$date, "time"=>$time, "temperature"=>$temperature);
    
    echo json_encode($arrayJSON);
?>
