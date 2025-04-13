#!/usr/bin/python

#<!-- Name: Kevin Olenic -->
#<!-- Username: ko19af -->
#<!-- St#: 6814974 -->

# get all the required imports
from os import environ
import cgi, cgitb, os

print "Content-Type: text/html"
print

#open and execute the top.cgi
exec(open("page/top.cgi").read()) #execute a file with javascript and html

# print the content on the other pages
print (open("page/FAQ.cgi").read())
print (open("page/bottom.cgi").read())
