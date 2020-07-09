#!/usr/bin/env python36
print("Content-Type: text/html\n")
import cgi ,cgitb
cgitb.enable()
import subprocess as sp
x=sp.getoutput("date")
import os
os.system("ssh localhost")

