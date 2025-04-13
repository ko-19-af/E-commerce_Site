#!/usr/bin/python

#<!-- Name: Kevin Olenic -->
#<!-- Username: ko19af -->
#<!-- St#: 6814974 -->

# get all the required imports
from pymongo import MongoClient
from os import environ
import cgi, cgitb, os

# log into database
un='ko19af'
passwd='6814974'
client=MongoClient('mongodb://'+un+':'+passwd+'@127.0.0.1/'+un)
db=client[un]

# create variable to check for foreign cookies
check = 0

# check if their is a cookie
if environ.has_key('HTTP_COOKIE'):
 # for each cookie get the key and value
 for cookie in map(str.strip, str.split(environ['HTTP_COOKIE'], ';')):
  (key, value) = str.split(cookie, '=');

  # if their is a cookie with key type and value admin
  if key=="type" and value=="admin":
   # set check to zero and exit for loop
   check = 0
   break

  # if their is a cookie with type user but not value admin
  if key=="type" and value!="admin":
   # redirect user back to login page
   print "Location:login.cgi"
   print

  # if their is a cookie that is not type user or foreign
  else:
   check = 1

# if no cookies present
else:
 # redirect back to login page
 print "Location:login.cgi"
 print

# if their is a cookie that is not of type user(foreign/non-user cookie)
if check==1:
 # redirect back to login page
 print "Location:login.cgi"
 print

# create form
form=cgi.FieldStorage()

# if their is a tag in the form
if "tag" in form:

 #get tag and product from the form and assign them to variables
 t=form.getfirst("tag")
 p=form.getfirst("product")

 # get product p from the database
 rec=db.products.find_one({'product':p})

 # if product dosen't exist print that no such product exist
 if rec==None:
  print "Content-Type: text/html"
  print
  print "<p>product does not exist</p>"

 # if add is in the form
 elif "add" in form:

  # if the tag is not in the products tags
  if t not in rec['tags']:

   # push tag t into product tags
   db.products.update({"product":p}, {"$push":{"tags":t}})
   # display tag was added
   print "Content-Type: text/html"
   print
   print "<p>Tag added</p>"

  else:
   # tag was not added
   print "Content-Type: text/html"
   print
   print "<p>Tag already exist</p>"

 elif "remove" in form:
  # push tag t into product tags
  db.products.update({"product":p}, {"$pull":{"tags":t}})
  # print that the tag was added
  print "Content-Type: text/html"
  print
  print "<p>Tag deleted</p>"

# if these items are in the form
if "product" in form and ("enable" in form or "disable" in form or "delete" in form):

 # get product name
 p=form.getfirst("product")

 # get record from database
 rec=db.products.find_one({'product':p})

 # if disable in form and thier is a record that matches the name
 if "disable" in form and rec!=None:

  # disable the product
  db.products.update({"product":p}, {"$set":{"status":"disable"}})

  # for every user remove the disables product
  for rec in db.users.find():
   # for every user pull the disabled product from their wishlist
   db.users.update({'user':rec['user']},{"$pull":{"products":p}})

  # print HTML and JavaScript content
  print "Content-Type: text/html"
  print
  # remove product from local storage and print product disabled
  print "<script>localStorage.removeItem('"+p+"');</script>"
  print "<p>Product Disabled</p>"
  
# if enable in form and thier is a record that matches the name
 elif "enable" in form and rec!=None:

  # enable the product
  db.products.update_one({"product":rec['product']}, {"$set":{"status":"show"}})
  print "Content-Type: text/html"
  print
  print "<p>Product Enabled</p>"

 #if delete is in the form and their is a product in the database with that name
 elif "delete" in form and rec!=None:
  # delete the product from database
  db.products.delete_one({"product":rec['product']})

  # for every user remove the deleted product
  for rec in db.users.find():
   # remove the deleted product from all user wishlists
   db.users.update({'user':rec['user']},{"$pull":{"products":p}})

  # print HTML and JavaScript content
  print "Content-Type: text/html"
  print
  # remove product from localstorage and print product deleted
  print "<script>localStorage.removeItem('"+p+"');</script>"
  print "<p>Product Deleted</p>"

 # if all the statements above are not satisfied
 else:
  print "Content-Type: text/html"
  print
  print "<p>Product Does not exist</p>"



# if create is in the form
if "create" in form:

 # get product information from the form
 prod=form.getfirst("productname")
 sdesc=form.getfirst("shortDescription")
 ldesc=form.getfirst("longDescription")
 cos=form.getfirst("price")
 pic=form.getfirst("image")
 t=form.getfirst("tags")

 # find any occurance of the product in the database
 rec=db.products.find_one({'product':prod})

 # if there is already a record with that product
 if rec!=None:
  print "Content-Type: text/html"
  print
  print "<p>product exist</p>"

 # if the product does not exist then add to database with the info
 else:
  print "Content-Type: text/html"
  print
  print "<p>product created</p>"
  # add product to the database
  db.products.insert_one({"product":prod,"tags":str.split(t, ','),"shortdesc":sdesc,"longdesc":ldesc,"price":cos,"image":pic,"status":"show"})


# execute the python and HTML content in the top.cgi page
exec(open("page/top.cgi").read()) #execute a file with javascript and html

print"""
<body>
<!-- Name: Kevin Olenic -->
<!-- Username: ko19af -->
<!-- St#: 6814974 -->

<!-- This sets the title of the page -->
<title>Product Admin Page</title>

<!-- print paragraph describing the purpose and functions of this page -->
<p>

<br>Welecome to the Product Admin page</br>

<br>If you are on this page then you are an admin or you got here via dubious ways</br>

<br>On this page you can do various Admin functions which are listed below</br>

<br>With This one you can enable/disable or delete a product</br>

</p>

<!-- create the form for taking info on product actions -->
<form name="productForm" method="post" action="#">

  <label for="product">Product:</label><br>
  <input type="text" name="product" required><br>
  <input type="submit" value="Enable" name="enable">
  <input type="submit" value="Disable" name="disable">
  <input type="submit" value="Delete" name="delete">


</form>

<!-- additional info -->

<p>

<br>With This one you can add/remove tags from a product</br>

</p>

<!-- create the form for taking info on product tag actions -->
<form name="productForm" method="post" action="#">

  <label for="product">Product:</label><br>
  <input type="text" name="product" required><br>
  <label for="tag">Tag:</label><br>
  <input type="text" name="tag" required><br>
  <input type="submit" value="Remove" name="remove">
  <input type="submit" value="Add" name="add">


</form>

<!-- additional info -->
<p>

<br>With This one you can create a product</br>

<br>Note: you must delimit the tags by commas e.g."horn,tail,purple"</br>

<br>Additional Note: you must input images in the form of Images/'product'.png</br>

<br>Sample Images: Moose.png, Robot.png, Hydra.png</br>

</p>

<!-- create the form for creating products -->
<form name="createProduct" method="post" action="#">

  <label for="productname">Product Name:</label><br>
  <input type="text" name="productname" required><br>

  <label for="shortDescription">Short Description:</label><br>
  <input type="text" name="shortDescription" required><br>

  <label for="longDescription">Long Description:</label><br>
  <input type="text" name="longDescription" required><br>

  <label for="price">Price($):</label><br>
  <input type="text" name="price" required><br>

  <label for="image">Image:</label><br>
  <input type="text" name="image" required><br>

  <label for="tags">Tags:</label><br>
  <input type="text" name="tags" required><br>

  <input type="submit" value="Create" name="create">

</form>
</body>
</html>
"""