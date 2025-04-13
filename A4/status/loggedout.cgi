#!/usr/bin/python

#<!-- Name: Kevin Olenic -->
#<!-- Username: ko19af -->
#<!-- St#: 6814974 -->

# get all the required imports
import cgi, cgitb, os

print"""
<body>
<!-- Name: Kevin Olenic -->
<!-- Username: ko19af -->
<!-- St#: 6814974 -->

<!-- This sets the title of the page -->
<title>Login</title>

<!-- print out page info -->
<p>

<br>Welecome to Monzilla a site that sells monsters that will probably kill you at unreasonable prices</br>

<br>You are currently not Logged Into this website (So shame on you)</br>

<br>If you want to Log in fill out both the username and password (p.s. check out what happens when you leave one field blank)<br>

<br>If you do not want to login then don't I can't force you to do anything (or can I)</br>

<br>Enjoy!!!!<b/r>

<br>p.s the nav bar will tell you if you are logged in or not by switching between out & in</br>

<br> If you have an account enter your username and password </br>

</p>

<!-- create form for receving username and password for login -->

<form name="loginForm" method="post" action="#">

  <label for="username">Username:</label><br>
  <input type="text" name="username" required><br>
  <label for="pass">Password:</label><br>
  <input type="password" name="pass" required><br><br>
  <input type="submit" value="Log In" name="created">

</form>

<!-- More page information -->

<p>

<br>If you want to create an account enter a unsername and password below </br>

</p>

<!-- create form for receving username and password for regeristing a user(create user) -->

<form name="signupForm" method="post" action="#">

  <label for="username">Username:</label><br>
  <input type="text" name="username" required><br>
  <label for="pass">Password:</label><br>
  <input type="password" name="pass" required><br><br>
  <input type="submit" value="Register" name="create">

</form>

</body>
</html>
"""