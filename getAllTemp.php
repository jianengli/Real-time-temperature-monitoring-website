<?php
	header("Access-Control-Allow-Origin:*");

	$splfileobject = new SplFileObject('TempInfo.txt', 'r');
	
	$splfileobject -> setCsvControl(',');
	
	$splfileobject -> setFlags(SplFileObject::READ_CSV);
	$arrayJSON = array();
	while(!$splfileobject -> eof()){
		
		$row = $splfileobject->current();

		if(count($row)==1) {
			break;
		}

		$arrayJSON[] = array("date"=>$row[0], "time"=>$row[1], "temperature"=>$row[2]);
		
		$splfileobject -> next();

	}
	
	echo  json_encode($arrayJSON);
?>