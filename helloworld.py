#!/usr/bin/python

print "Content-Type: text/html"
print "<p>Hello World</p>"

def my_function():
  print("Hello from a function")

my_function()


default_app = firebase_admin.initialize_app()