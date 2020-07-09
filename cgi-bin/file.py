#!/usr/bin/python36
#importing python modules
import subprocess as sp
import cgi

print("content-type: text/html")

#variables
form=cgi.FieldStorage()
filepath=str(form.getvalue("File_Path"))
own=str(form.getvalue("File_Own"))
grp=str(form.getvalue("File_Group"))
mod=str(form.getvalue("Mode"))

sp.getoutput("sudo chmod 0777 /var/www/cgi-bin/filevar.yml")
#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/filevar.yml",mode='w')

#writing varibles in file
fp.write('filepath: "{}"\n'.format(filepath))
fp.write('own: "{}"\n'.format(own))
fp.write('grp: "{}"\n'.format(grp))
fp.write('mod: "{}"\n'.format(mod))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("sudo ansible-playbook file.yml")
print("location: http://192.168.43.228/menu.html\n")
