#!/usr/bin/python36
print("content-type: text/html")
import cgi
form=cgi.FieldStorage()
name=str(form.getvalue("User_Name"))
passwd=str(form.getvalue("Password"))

if name=="cloud" and passwd=="prabhat":
	print("location: http://192.168.43.228/main.html\n")
else:

	print("location: http://192.168.43.228/index.html\n")
