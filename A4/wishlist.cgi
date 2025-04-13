#!/usr/bin/python

#<!-- Name: Kevin Olenic -->
#<!-- Username: ko19af -->
#<!-- St#: 6814974 -->

# get all the required imports
from os import environ
import cgi, cgitb, os

print "Content-Type: text/html"
print

# execute the python and HTML content in the top page
exec(open("page/top.cgi").read())

# create link to switch to printable wishlist
print "<a href='print.cgi'> Click to change into printable wishlist</a>"

# print the content in the wishlist and bottom page
print (open("page/wishlist.cgi").read())
print (open("page/bottom.cgi").read())
