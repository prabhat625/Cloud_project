#!/usr/bin/python36


import subprocess as sp
import cgi

print("content-type: text/html\n")

form=cgi.FieldStorage()

size=int(form.getvalue("size"))
size=size*1024*1024
username="root"
passwd=str(form.getvalue("Password"))
ip=str(form.getvalue("Ip"))

#print(username)
#print(passwd)
#print(ip)
#print(size)



###############  generate starting and ending size of block  ############

string = sp.getoutput("sudo fdisk -l /dev/sdb")
list=string.split("\n")
number=int(((list[-1].split(" "))[0])[-1])+1

start=(list[-1].split(" ")[16])
list1=(list[-1].split())
list2=[]
for x in list1:
    if x!=" ":
       list2.append(x)


start=list2[2]
start =int(start)
start =start +100
start=start*512
start=(start/1024)

end=start+size

start=int(start)
end=int(end)

########  writing variables in file  ###############

fp=open("/var/www/cgi-bin/staas/var.yml","w")
fp.write('number: "{}"\n'.format(number))
fp.write('start: "{}"\n'.format(start))
fp.write('end: "{}"\n'.format(end))
fp.write('passwd: "{}"\n'.format(passwd))
fp.write('username: "{}"\n'.format(username))
fp.write('ip: "{}"\n'.format(ip))
fp.close()

x=sp.getoutput("sudo ansible-playbook form.yml")
#print("bdioqwbidvq")

fp=open("userset.yml","r")
ch=fp.read()
fp.close()
String ="- hosts: "+str(username)+str(number)+"\n"
fp1=open("setuser.yml","w")
fp1.write(String)
fp1.write(ch)
fp1.close()


print(''' <body bgcolor="black"><center><div   class="button button4" style="padding:10px ; font-size:25px ; background-color:black ;margin:36%"><a href="./staas2.py" target="_blank"><font color="white">Buy Now</font></div></center></body>''')
