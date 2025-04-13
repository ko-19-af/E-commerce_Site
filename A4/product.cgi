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

# get product id
pid = form.getfirst("id")

# get record that has that product id
rec=db.products.find_one({'product':pid})

exec(open("page/top.cgi").read())

# redirect back to products if prouct has been disabled (user tries to force their way to a product)
if rec==None or str(rec['status'])!="show":
 print "<p> Requested product does not exist or was removed</p>"
 print


# if product status is show print the products information
elif str(rec['status'])=="show":

 print"""
 <script>
 window.addEventListener('load',loadList)
 </script>
 """

 print "<title>"+rec['product']+"</title>"

 print "<h1>Product -"+rec['product']+"</h1>"

 print "<img src='"+rec['image']+"'alt="+rec['product']+">"

 print "<pre>"+rec['shortdesc']+"</pre>"

 print "<!-- This button will add the product to local storage and activate other related functions-->"

 print """<button id='Button_"""+rec['product']+"""' onclick="saveToStorage('"""+rec['product']+"""')">Add To Wishlist</button>"""


 print"""<!-- This will show the object that are wishlisted and hold the buttons for adding and removing products -->
 <pre id="wishList">Products In WishList:

 </pre>
 """

# print the bottom page info
print(open("page/bottom.cgi").read())