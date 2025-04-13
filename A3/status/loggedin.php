<html>
<head>

<!-- This sets the title of the page -->
<title>LogOut</title>

<script>

// create event listner that loads the wishlist for when the window loads/reloads
window.addEventListener('load',serverSave)

</script>

</head>

<body>

<p>

<br>You are currently Logged Into this website (So congratulations to you)</br>

<br>Your wishlist will now be saved to the server</br>

<br>If you want to Log out press the button below<br>

<br>If you do not want to logout then don't press the button</br>

<br>Also F.Y.I you will automatically be logged out after about two hours</br>

<br>Enjoy!!!!<b/r>

</p>

<form name="myForm" action="login.php" method="post">

  <input type="submit" value="Log out">

</form>
</body>
</html>

<?php

// if server request method is post
if ($_SERVER["REQUEST_METHOD"] == "POST") {

	// remove user cookie
	setcookie("user", "", time() - 3600);

	//refresh page
	header("refresh: 0");
}
?>