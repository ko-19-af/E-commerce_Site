<header>
<!-- Name: Kevin Olenic -->
<!-- Username: ko19af -->
<!-- St#: 6814974 -->

<!-- this sets the css stylesheet -->
<link rel="stylesheet" type="text/css" href="StyleSheet.css">

<!-- this sets the java script sources for the page -->
<script src="Script.js"></script>

<nav>

<!-- This creates the nav bar -->
<ul>
<li class="navigate"><a href ="main.php">Main Page</a>

<li class="navigate"><a href="products.php">Products</a>

<li class="navigate"><a href="contact.php">Contact</a>

<li class="navigate"><a href="FAQ.php">FAQ</a>

<li class="navigate"><a href="wishlist.php">WishList</a>

<?php
// if user cookie is set
if(!isset($_COOKIE["user"])) {
	
	echo '<li class="navigate"><a href="login.php">Currently Logged Out</a>';
} 

// if user cookie is not set
else {

	echo '<li class="navigate"><a href="login.php">Currently Logged In</a>';
}
?>

</nav>

</header>