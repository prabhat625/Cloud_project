#!/usr/bin/python36
#importing python modules
import subprocess as sp
import cgi 

print("content-type: text/html")
#variables
form=cgi.FieldStorage()
name=form.getvalue("Service")
status=form.getvalue("Service_stat")

#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/servicevar.yml",mode='w')

#writing varibles in file
fp.write('name: "{}"\n'.format(name))
fp.write('state: "{}"\n'.format(status))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("sudo ansible-playbook service.yml")
print("location: http://192.168.43.228/menu.html\n")
