#!/usr/bin/python36
#importing python modules
import subprocess as sp
import cgi

print("content-type: text/html")
#variables
form=cgi.FieldStorage()
filesrc=str(form.getvalue("Src_Path"))
filedest=str(form.getvalue("Dest_Path"))
sp.getoutput("sudo chmod 0777 /var/www/cgi-bin/copyvar.yml")

#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/copyvar.yml",mode='w')
#writing varibles in file
fp.write('srcfile: "{}"\n'.format(filesrc))
fp.write('destfile: "{}"\n'.format(filedest))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("sudo ansible-playbook copy.yml")
print("location: http://192.168.43.227/menu.html\n")
