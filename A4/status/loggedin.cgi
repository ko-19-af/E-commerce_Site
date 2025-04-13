#!/usr/bin/python

#<!-- Name: Kevin Olenic -->
#<!-- Username: ko19af -->
#<!-- St#: 6814974 -->

# get all the required imports
from os import environ
import cgi, cgitb, os

print """
<html>
<head>

<!-- This sets the title of the page -->
<title>LogOut</title>

<script>

// create event listner that loads the wishlist for when the window loads/reloads(sync local with server wishlist)
window.addEventListener('load',serverSave)

</script>

</head>

<body>

<!-- print page information -->

<p>

<br>You are currently Logged Into this website (So congratulations to you)</br>

<br>Your wishlist will now be saved to the server</br>

<br>If you want to Log out press the button below<br>

<br>If you do not want to logout then don't press the button</br>

<br>Also F.Y.I you will automatically be logged when you leave this session</br>

<br>Enjoy!!!!<b/r>

</p>

<!-- create form for logging out -->

<form name="myForm" action="" method="post">

  <input type="submit" value="Log out" name="logout">

</form>
</body>
</html>
"""
