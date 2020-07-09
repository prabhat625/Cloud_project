#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")


form=cgi.FieldStorage()

name = form.getvalue("name")
string ="sudo docker stop "+str(name)
x=sp.getoutput(string)
print("location: http://192.168.43.228/cgi-bin/docker.py\n")
