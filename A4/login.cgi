#!/usr/bin/python

#<!-- Name: Kevin Olenic -->
#<!-- Username: ko19af -->
#<!-- St#: 6814974 -->

# get all the required imports
from pymongo import MongoClient
from os import environ
import cgi, os, base64

# log into database
un='######'
passwd='#######'
client=MongoClient('mongodb://'+un+':'+passwd+'@127.0.0.1/'+un)
db=client[un]

#create fieldstorage with form data
form=cgi.FieldStorage()

# load server wishlist into local wishlist
def sync_func(rec):
 # if their are products in the server storage
 if len(rec['products'])!=0:

  # add each product in server storage to localstorage
  for p in rec['products']:
   print """
   <script>
   // load all elements from user server storage to local storage
   localStorage.setItem('"""+p+"""', '"""+p+"""');
   </script>
   """

  #reload the page when a user logs in
  print"""
  <script> 
  // reload login page (so as to go to logged in page
  window.location.href="login.cgi";
  </script>
  """
#if username and password and create in the form  create a new user
if "username" in form and "pass" in form and "create" in form:

 #get username and password and assign to variables
 name=form.getfirst("username")
 password=form.getfirst("pass").encode("utf-8")

 # encrypt the password using base 64
 encrypt=base64.b64encode(password)

 #check for user with entered username
 rec=db.users.find_one({'user':name})

 #if no rec of user with same user name exist
 if rec==None:
  #insert the new user into the users database
  db.users.insert_one({"user":name,"pwd":encrypt,"type":"user","products":[]})
  # set the cookie login for the new user
  print "Set-Cookie:user="+name
  print "Set-Cookie:type=user"
  print "Location:login.cgi"
  print
  exit()

 #if thier is a record with that username
 else:
   print "Content-Type: text/html"
   print
   print "<p>Invalid entry user already exist</p>"

#if username and password in the form created is in form
if "username" in form and "pass" in form and "created" in form:
 
 name=form.getfirst("username")
 password=form.getfirst("pass").encode("utf-8")

 # encrypt the password
 encrypt=base64.b64encode(password)

 #get record with corresponding username
 rec=db.users.find_one({'user':name})

 # if there is no record with that username
 if rec==None:
  print "Content-Type: text/html"
  print
  print "<p> Invalid username or password</p>"

 # if there is a record with that username
 else:
  # if the password entered(encrypted) matches the password in the database(encrypted)
  if str(encrypt)==rec['pwd'] and str(rec['type'])!="disable":
   print "Set-Cookie:user="+name
   print "Set-Cookie:type="+rec['type']
   sync_func(rec)
   print "Location:login.cgi"
   print
   exit()

  # if the user has been disabed print user disabled
  elif str(rec['type'])=="disable":
   print "Content-Type: text/html"
   print
   print "<p> Invalid user disdabled</p>"

  # if they do not match
  else:
   print "Content-Type: text/html"
   print
   print "<p> Invalid username or password</p>"

# create check variable for cookies that do not satisfy conditions
check = 0

if "logout" in form:
 for cookie in map(str.strip, str.split(environ['HTTP_COOKIE'], ';')):
  print "Set-Cookie:"+cookie+";expires=Sat, 7-Feb-2000 03:10:00;"
  print "Location:login.cgi"

# execute the python and HTML code in the top page
exec(open("page/top.cgi").read()) #execute a file with javascript and html

# if their is a cookie(s)
if environ.has_key('HTTP_COOKIE'):

 # for each cookie get the key and value
 for cookie in map(str.strip, str.split(environ['HTTP_COOKIE'], ';')):
  (key, value) = str.split(cookie, '=');

  #if key of cookie is user or admin load the logged in page and break out of loop
  if key=="type" and (value=="user" or value=="admin"):
   exec(open("status/loggedin.cgi").read())
   check = 0 # set check to zero
   break # and break

  # if key is not type or value is not user or admin set check to 1
  else:
   check = 1

# if their are no cookies
else:
 # execute the loggedout.cgi page
 exec(open("status/loggedout.cgi").read())

# if their is a cookie and does not satisfy conditions
if check==1:
 # execute the loggedout.cgi page
 exec(open("status/loggedout.cgi").read())

# print the contents of the bottom page
print (open("page/bottom.cgi").read())