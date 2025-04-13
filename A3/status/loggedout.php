<body>
<!-- Name: Kevin Olenic -->
<!-- Username: ko19af -->
<!-- St#: 6814974 -->

<!-- This sets the title of the page -->
<title>Login</title>

<p>

<br>Welecome to Monzilla a site that sells monsters that will probably kill you at unreasonable prices</br>

<br>You are currently not Logged Into this website (So shame on you)</br>

<br>If you want to Log in fill out both the username and password (p.s. check out what happens when you leave one field blank)<br>

<br>If you do not want to login then don't I can't force you to do anything (or can I)</br>

<br>Also F.Y.I you will automatically be logged out after about two hours</br>

<br>Enjoy!!!!<b/r>

<br>p.s the nav bar will tell you if you are logged in or not by switching between out & in</br>

</p>


<form onsubmit="load()" name="myForm" action="login.php" method="post">

  <label for="username">Username:</label><br>
  <input type="text" name="username" required><br>
  <label for="pwd">Password:</label><br>
  <input type="password" name="pwd" required><br><br>
  <input type="submit" value="Log In">

</form>

</body>
</html>

<script>

// load items from server
function load(){

	var x = document.forms["myForm"]["username"].value;
	var y = document.forms["myForm"]["pwd"].value;

	// if username and password are not empty
	if (x !== "" && y !== "" ){

		// create xmlhttp request
		var xhttp = new XMLHttpRequest();
		//on ready state
  		xhttp.onreadystatechange = function(){

			if (this.readyState == 4 && this.status == 200){
				// load every line of serverlist into localstorage
      		   		text = this.responseText;
				lines = text.split("\n");
				for(i = 0; i < lines.length; i++){
					// add item to local storage
            				localStorage.setItem(lines[i], lines[i]);
			}
		}
  	};

	// open server list file
 	xhttp.open("GET", "serverlist.txt", true);

	// send request
	xhttp.send(); 
	}
}
</script>

<?php

// if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST"){

	// if password and username is empty do nothing
	if (empty($_POST["pwd"]) and empty($_POST["username"])){
	}

	// if username is empty do nothing
	elseif (empty($_POST["username"])){
	}
	// if password is empty do nothing
	elseif (empty($_POST["pwd"])){
	}

	else{
		// set user cookie name and value
		$cookie_name = "user";
		$cookie_value = "user";
		// set cookie
		setcookie($cookie_name, $cookie_value, time() + (86400)); // 86400 = 1 day

		// refresh page(it will change to the logged in page after a succesful login)
		header("refresh: 0");
	}
}
?>