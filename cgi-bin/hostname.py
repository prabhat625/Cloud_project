#!/usr/bin/python36
#importing python modules
import subprocess as sp
import cgi

print("content-type: text/html")

form=cgi.FieldStorage()
#variables
host=str(form.getvalue("Hostname"))

sp.getoutput("sudo chmod 0777 /var/www/cgi-bin/hostvar.yml")
#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/hostvar.yml",mode='w')

#writing varibles in file
fp.write('host: "{}"\n'.format(host))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("sudo ansible-playbook hostname.yml")
print("location: http://192.168.43.228/menu.html\n")

