#!/usr/bin/python

#<!-- Name: Kevin Olenic -->
#<!-- Username: ko19af -->
#<!-- St#: 6814974 -->

# get all the required imports
from os import environ
import cgi, cgitb, os

# execute the HTML and python code in the top.cgi page
exec(open("page/top.cgi").read()) #execute a file with javascript and html

print"""

<script>

// create event listner that loads the wishlist for when the window loads/reloads in printable form
window.addEventListener('load',load)

</script>

"""

# add link to return to original wishlist
print "<a href='wishlist.cgi'> Click to change to return to wishlist</a>"

# print the HTML content in the print and bottom pages
print(open("page/print.cgi").read())
print (open("page/bottom.cgi").read())
