#!/usr/bin/python

#<!-- Name: Kevin Olenic -->
#<!-- Username: ko19af -->
#<!-- St#: 6814974 -->

# get all the required imports
from os import environ
import cgi, cgitb, os

print "Content-Type: text/html"
print

# execute the top.cgi which contains both python and HTML content
exec(open("page/top.cgi").read()) #execute a file with javascript and html

# print the pages with HTML content
print (open("page/main.cgi").read())
print (open("page/bottom.cgi").read())
