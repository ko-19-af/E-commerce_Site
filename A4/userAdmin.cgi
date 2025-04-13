#!/usr/bin/python

#<!-- Name: Kevin Olenic -->
#<!-- Username: ko19af -->
#<!-- St#: 6814974 -->

# get all the required imports
from pymongo import MongoClient
from os import environ
import cgi, os

# log into database
un='ko19af'
passwd='6814974'
client=MongoClient('mongodb://'+un+':'+passwd+'@127.0.0.1/'+un)
db=client[un]

# create form
form=cgi.FieldStorage()

# create variable to check for foreign cookies
check = 0

# check if their is a cookie
if environ.has_key('HTTP_COOKIE'):
 # for each cookie get the key and value
 for cookie in map(str.strip, str.split(environ['HTTP_COOKIE'], ';')):
  (key, value) = str.split(cookie, '=');

# if their is a cookie with type user and value admin
  if key=="type" and value=="admin":
   check = 0
   break

  # if their is a cookie with type user but not value admin
  if key=="type" and value!="admin":
   print "Location:login.cgi"
   print

  # if their is a cookie that is not type user or foreign
  else:
   check = 1

# if no cookies present redirect to login
else:
 print "Location:login.cgi"
 print

# if their is a cookie that is not of type user(foreign/non-user cookie) redirect to login
if check==1:
 print "Location:login.cgi"
 print

# if username is in the form
if "username" in form:

 # get the name from the form and assign it to a variable
 name=form.getfirst("username")

 #get the record with the username from the database
 rec=db.users.find_one({'user':name})

 # if disable in form and it exist in the database
 if "disable" in form and rec!=None:

  #disable user based on user name and print user disabled
  db.users.update_one({"user":rec['user']}, {"$set":{"type":"disable"}})
  print "Content-Type: text/html"
  print
  print "<p>user Disabled</p>"

 # if delete in form and it exist
 if "delete" in form and rec!=None:

  # delete user from database based on username and print it was deleted
  db.users.delete_one({"user":rec['user']})
  print "Content-Type: text/html"
  print
  print "<p>User Deleted</p>"

 # if no user exist in the database print user does not exist
 if rec==None:
  print "Content-Type: text/html"
  print
  print "<p>Invalid no such user exist</p>"

# execute the python and HTML code in the top page
exec(open("page/top.cgi").read())

print"""
<body>
<!-- Name: Kevin Olenic -->
<!-- Username: ko19af -->
<!-- St#: 6814974 -->

<!-- This sets the title of the page -->
<title>User Admin Page</title>

<!-- print out page information -->
<p>

<br>Welecome to the Product Admin page</br>

<br>If you are on this page then you are an admin or you got here via dubious ways</br>

<br>On this page you can do various Admin functions which are listed below</br>

<br>In the one below you can disable or delete an account</br>

</p>

<!-- create form for taking admin actions on user -->
<form name="disable" method="post" action="#">

  <label for="username">Username:</label><br>
  <input type="text" name="username" required><br>
  <input type="submit" value="Disable" name="disable">
  <input type="submit" value="Delete" name="delete">

</form>
</body>
</html>
"""