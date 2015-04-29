<?php
    $myFile = "data";
    $fh = fopen($myFile, 'a') or die("can't open file");
    $stringData = $_GET['data']."\n";
    fwrite($fh, $stringData);
    echo $_GET['data'];
?>
