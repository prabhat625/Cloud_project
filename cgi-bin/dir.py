#!/usr/bin/python36
#importing python modules
import subprocess as sp
import cgi

print("content-type: text/html")

form=cgi.FieldStorage()
#variables
dirpath=str(form.getvalue("Dir_Name"))
own=str(form.getvalue("Own_Name"))
grp=str(form.getvalue("Grp_Name"))
mod=str(form.getvalue("Mode"))


sp.getoutput("sudo chmod 0777 /var/www/cgi-bin/dirvar.yml")
#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/dirvar.yml",mode='w')

#writing varibles in file
fp.write('dirpath: "{}"\n'.format(dirpath))
fp.write('own: "{}"\n'.format(own))
fp.write('grp: "{}"\n'.format(grp))
fp.write('mod: "{}"\n'.format(mod))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("sudo ansible-playbook dir.yml")
print("location: http://192.168.43.228/menu.html\n")
