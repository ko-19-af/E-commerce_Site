#!/usr/bin/python

print """
<header>
<!-- Name: Kevin Olenic -->
<!-- Username: ko19af -->
<!-- St#: 6814974 -->

<!-- this sets the css stylesheet -->
<link id="style" rel="stylesheet" type="text/css" href="StyleSheet.css">

<!-- this sets the java script sources for the page -->
<script src="Script.js"></script>

<!--This is the common banner for the assignment, everypage has this in it as every page uses the nav bar and stylesheet -->

<nav>

<!-- This creates the nav bar -->
<ul>
<li class="navigate"><a href ="main.cgi">Main Page</a>

<li class="navigate"><a href="products.cgi">Products</a>

<li class="navigate"><a href="contact.cgi">Contact</a>

<li class="navigate"><a href="FAQ.cgi">FAQ</a>

<li class="navigate"><a href="wishlist.cgi">WishList</a>

<li class="navigate"><a href="#" id="change">Change Theme</a>

<script>
// create button linked to change theme button in nav bar
button = document.getElementById("change");
// add event listener on click that calls change method
button.addEventListener("click",change);
// call change sheet to decide which style sheet is to be used
changeSheet();

// function for adding item to local storage fo deciding which style sheet to use
function change(event) {

        // get style sheet
	sheet = document.getElementById("style");

        // if change style in session storage
	if ("changestyle" in sessionStorage){
                // remove change style from session storage
		sessionStorage.removeItem("changestyle");
                // and set stylesheet back to original sheet
		sheet.setAttribute("href","StyleSheet.css");
	}
        // if change style not in session storage
	else{
                // put change style in session storage
		sessionStorage.setItem("changestyle","changestyle");
                // and set to alternate style sheet
		sheet.setAttribute("href","altstyle.css");
	}
}

// function to decide if we are going to change the style sheet
function changeSheet(){
        // if change style in local storage
	if ("changestyle" in sessionStorage){
                // get stylesheet link by id
		sheet = document.getElementById("style");
                // set link to alternate stylesheet
		sheet.setAttribute("href","altstyle.css");
	}
}
</script>

"""

# create variable check for checking 
check = 0

# check if their is a cookie
if environ.has_key('HTTP_COOKIE'):
 # for each cookie get the seperate the key and value
 for cookie in map(str.strip, str.split(environ['HTTP_COOKIE'], ';')):
  (key, value) = str.split(cookie, '=');
  
   #if key of cookie is user create user nav bar options
  if key=="type" and value=="user":
   print "<li class='navigate'><a href='login.cgi'>Logged In: "+value+"</a>"
   check = 0 # set check to zero
   break # break out of the loop

   # if key of cookie is admin create admin nav bar options
  elif key=="type" and value=="admin":
   print "<li class='navigate'><a href='login.cgi'>Logged In: "+value+"</a>"
   print "<li class='navigate'><a href='userAdmin.cgi'>User Admin</a>"
   print "<li class='navigate'><a href='prodAdmin.cgi'>Product Admin</a>"
   check = 0 # set check to zero
   break # break out of the loop

  # if above conditions are not satisfied set check to one
  else:
   check = 1

# if there is no cookie create logged out in nav bar
else:
   print "<li class='navigate'><a href='login.cgi'>Logged Out</a>"

# if their is only a cookie and does not satisfy conditions(in case of foreign cookies)
if check==1:
 print "<li class='navigate'><a href='login.cgi'>Logged Out</a>"

print "</nav>"
print "</header>"