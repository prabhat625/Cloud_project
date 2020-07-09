#!/usr/bin/python36
#importing python modules
import subprocess as sp
import cgi

print("content-type: text/html")

#variables
form=cgi.FieldStorage()
conname=str(form.getvalue("Con_Name"))
ifnam=str(form.getvalue("Network_Card_Name"))
typ=str(form.getvalue("Network_Card_Type"))
ip=str(form.getvalue("Ip"))
gw=str(form.getvalue("Gateway"))
dns=str(form.getvalue("Dns"))

sp.getoutput("sudo chmod 0777 /var/www/cgi-bin/staticvars.yml")

#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/staticvars.yml",mode='w')

#writing varibles in file
fp.write('conname: "{}"\n'.format(conname))
fp.write('ifnam: "{}"\n'.format(ifnam))
fp.write('type: "{}"\n'.format(typ))
fp.write('dns: "{}"\n'.format(dns))
fp.write('ip: "{}"\n'.format(ip))
fp.write('gw: "{}"\n'.format(gw))

#closing file
fp.close()
#running ansible playbook
x=sp.getoutput("sudo ansible-playbook staticip.yml")
print("location: http://192.168.43.228/menu.html\n")
