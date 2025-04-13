#!/usr/bin/php-cgi

<html>
<!-- Name: Kevin Olenic -->
<!-- Username: ko19af -->
<!-- St#: 6814974 -->

<body>

<?php
include 'top.php';
include 'bottom.php';
include "Products/" . $_GET['id'] . ".php";
?>

</body>
</html>