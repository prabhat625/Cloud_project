#!/usr/bin/python36
#importing python modules

import subprocess as sp
import cgi

print("content-type: text/html")
form=cgi.FieldStorage()

#variables
username=form.getvalue("User_Name")
username=str(username)

sp.getoutput("sudo chmod 0777 /var/www/cgi-bin/uservar.yml")

#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/uservar.yml",mode='w')

#writing varibles in file
fp.write('username: "{}"\n'.format(username))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("sudo ansible-playbook user.yml")

print("location: http://192.168.43.228/menu.html\n")
