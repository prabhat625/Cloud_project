#!/usr/bin/python36
#importing python modules
import subprocess as sp
import cgi

print("content-type: text/html")
#variables
form=cgi.FieldStorage()
filesrc=str(form.getvalue("Src_Path"))
filedest=str(form.getvalue("Dest_Path"))
form=str(form.getvalue("Format"))

sp.getoutput("sudo chmod 0777 /var/www/cgi-bin/tarvar.yml")
#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/tarvar.yml",mode='w')

#writing varibles in file
fp.write('filesrc: "{}"\n'.format(filesrc))
fp.write('filedest: "{}"\n'.format(filedest))
fp.write('form: "{}"\n'.format(form))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("sudo ansible-playbook archive.yml")
print("location: http://192.168.43.228/menu.html\n")
