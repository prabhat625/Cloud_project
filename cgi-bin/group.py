#!/usr/bin/python36
#importing python modules
import subprocess as sp
import cgi

print("content-type: text/html")

#variables
form=cgi.FieldStorage()
grpname=form.getvalue("Group_Name")
grpname=str(grpname)
sp.getoutput("sudo chmod 0777 /var/www/cgi-bin/groupvar.yml")

#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/groupvar.yml",mode='w')

#writing varibles in file
fp.write('grpname: "{}"\n'.format(grpname))

#closing file
fp.close()
#running ansible playbook
x=sp.getoutput("sudo ansible-playbook group.yml")
print("location: http://192.168.43.228/menu.html\n")
