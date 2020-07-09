#!/usr/bin/python36
#importing python modules
import subprocess as sp
import cgi
print("content-type: text/html")
#variables
form=cgi.FieldStorage()
packname=str(form.getvalue("Package"))


sp.getoutput("sudo chmod 0777 /var/www/cgi-bin/softvars.yml")
#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/softvars.yml",mode='w')

#writing varibles in file
fp.write('packname: "{}"\n'.format(packname))

#closing file
fp.close()


#running ansible playbook
x=sp.getoutput("sudo ansible-playbook software.yml")
print("location: http://192.168.43.228/menu.html\n")

