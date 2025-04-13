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

#create fieldstorage with form data
form=cgi.FieldStorage()

# get product tag
t = form.getfirst("tag")

# execute the python and HTML content in the top and product pages
exec(open("page/top.cgi").read()) #execute a file with javascript and html
exec(open("page/products.cgi").read())

# print info on how to use filter
print """<p>Use this to search  for products based on tags enter multiple tags to search for multiple products e.g. purple,horns,blue, Note: enter a blank field to get back all products</p>
<p>Sample tags: "horns", "tentacles", "tail", "purple", "blue", "tail", "green" </p>"""

# create form to filter products by tags
print"""<form name="disable" method="post" action="#">

  <label for="tag">Enter Tag:</label><br>
  <input type="text" name="tag"><br>
  <input type="submit" value="Search">

</form>
"""
# if there is a tag(s) that the user wants to look for specefically
if t != None:

 #Split the tags by comma seperators
 split = t.split(",")

 #for every tag in the split
 for tag in split:

  # find all products that contain the tag
  prods=db.products.find({'tags':tag})

  # if there are products that have the desired tag
  if prods!=None:
   # go through all the products that have the tags:t and print the info
   for rec in prods:

    if str(rec['status'])=="show":
     print "<h1>Product -"+rec['product']+"</h1>"

     print """<a href="product.cgi?id="""+rec['product']+"""">

     <img src='"""+rec['image']+"""' alt="Unavailable">
     </a>
     """
     print "<!-- This button will add the product to local storage and activate other related functions-->"
     print """<button id='Button_"""+rec['product']+"""' onclick="saveToStorage('"""+rec['product']+"""')">Add """+rec['product']+""" To Wishlist</button>"""
     print "<pre>"+rec['longdesc']+"</pre>"

else:
 # go through all the products that have the status:show and print them
 for rec in db.products.find({'status':'show'}):

  print "<h1>Product -"+rec['product']+"</h1>"

  print """<a href="product.cgi?id="""+rec['product']+"""">

  <img src='"""+rec['image']+"""' alt="Unavailable">
  </a>
  """

  print "<!-- This button will add the product to local storage and activate other related functions-->"
  print """<button id='Button_"""+rec['product']+"""' onclick="saveToStorage('"""+rec['product']+"""')">Add """+rec['product']+""" To Wishlist</button>"""
  print "<pre>"+rec['longdesc']+"</pre>"

# print the bottom page
print(open("page/bottom.cgi").read())
