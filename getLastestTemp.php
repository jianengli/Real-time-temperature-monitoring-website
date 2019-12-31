<?php
    header("Access-Control-Allow-Origin:*");	
    header('Content-Type: text/event-stream');
    header('Cache-Control: no-cache');

    $file = new SplFileObject("TempInfo.txt",'r');
    $str = "";

    $file->seek($file->getSize());
    $linesTot = $file->key();

    $file->seek($linesTot-1);
    echo "data: ".$file->current()."\n\n";
    
    flush();
?>
