#!/usr/bin/php-cgi

<html>
<!-- Name: Kevin Olenic -->
<!-- Username: ko19af -->
<!-- St#: 6814974 -->

<body>

<?php
include 'top.php';
include 'bottom.php';

// if user cookie is set
if(!isset($_COOKIE["user"])){

	// go to loggedout page
	include "status/loggedout.php";
} 

// if user cookie is not set
else {
	// go to loggedin page
	include "status/loggedin.php";
}
?>

</body>
</html>