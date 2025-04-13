#!/usr/bin/php-cgi

<?php
// Start the session
session_start();
?>

<?php
// Name: Kevin Olenic
// Username: ko19af
// St#: 6814974

// make action and product global
$q = $_REQUEST["id"];
$v = $_REQUEST["product"];

// if user cookie is present (if user is logged in)
if(isset($_COOKIE["user"])){

	// if action is add
	if($q == "add" && ($v !== "" || $v !==" ")){

		// open serverlist file (if there is not one it will create it)
		$myfile = fopen("serverlist.txt", "a") or die("Unable to open file!");

		// add product as new line in file
		fwrite($myfile, $v."\n");
		// close file
		fclose($myfile);
	}

	//if action is remove
	elseif($q == "remove"){
		
		// get contents of the file
		$str = file_get_contents("serverlist.txt");

		// replace all instances of product being removed
		$str = str_replace($product,"",$product);
		
		// put strings back into file
		file_put_contents("serverlist.txt",$str);
	}
}
?>