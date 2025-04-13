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

# create form
form=cgi.FieldStorage()

# create variables that hold the product and action being used
action=form.getfirst("id")
p=form.getfirst("product")

# if their is a cookie
if environ.has_key('HTTP_COOKIE'):
 # for each cookie get the seperate the key and value
 for cookie in map(str.strip, str.split(environ['HTTP_COOKIE'], ';')):
  (key, value) = str.split(cookie, '=');

  # if the key is of type
  if key=="user":
   # get record with corresponding username
   rec=db.users.find_one({'user':value})
   
   # if action is add and p is not in the records products
   if action=="add" and p not in rec['products']:
    #push the product into the users server wishlist
    db.users.update({"user":value}, {"$push":{"products":p}})
    print

   #if action is remove
   if action=="remove":
    # pull product from user wishlist
    db.users.update({"user":value}, {"$pull":{"products":p}})
    print
