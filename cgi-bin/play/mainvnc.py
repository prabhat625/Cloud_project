#!/usr/bin/python36
import subprocess as sp
import cgi
import random
print("content-type: text/html\n")
#vnc_server --vnc 192.168.43.227:5905

form=cgi.FieldStorage()
name=str(form.getvalue("User_Name"))
passwd=str(form.getvalue("Password"))

storage=sp.getoutput("sudo id {}".format(name))
lil=storage.split(" ")
if "no" in lil:
	String = sp.getoutput("sudo netstat -tnlp")
	list1=String.split("\n")
	list4=[""]

	for i in range(1,len(list1)):
	        list2=list1[i].split()
	        list3=list2[3].split(":")
	        list4.extend(list3)






	#form =cgi.FieldStorage()
	#name=str(form.getvalue("name"))
	#image=str(form.getvalue("image"))
	port=random.randrange(5905,5999,1)

	port=str(port)
	while port in list4:
		port=str(random.randrange(5905,5999,1))
	

	port=int(port)
	port=port%100

	portc=random.randrange(6000,9999,1)

	portc=str(portc)
	while portc in list4:
	        portc=str(random.randrange(6000,9999,1))
	portc=int(portc)

	portd=port+5900

	fp=open("/var/www/cgi-bin/play/vncvar.yml","w")
	fp.write('user: "{}"\n'.format(name))
	fp.write('passwd: "{}"\n'.format(passwd))
	fp.write('prt: "{}"\n'.format(port))
	fp.write('prt1: "{}"\n'.format(portc))
	fp.write('prt2: "{}"\n'.format(portd))
	fp.close()

	
	sp.getoutput("sudo ansible-playbook vnc.yml")
	


	fp=open("vncuser.yml","r")
	ch=fp.read()
	fp.close()
	String ="- hosts: "+name+"\n"
	fp1=open("everyvnc.yml","w")
	fp1.write(String)
	fp1.write(ch)
	fp1.close()
	

	


	sp.getoutput("sudo ansible-playbook everyvnc.yml")


	print(''' <body bgcolor="black"><center><div   class="button button4" style="padding:10px ; font-size:25px ; background-color:black ;margin:36%"><a href="./page2.py?port={}&portc={}"><font color="green">Launch Instance</font></div></center></body>'''.format(port,portc))
	

	



	


	#sp.getoutput("sudo systemctl daemon-reload")

	#sp.getoutput("sudo systemctl restart vncserver@:"+str(port)+".service")
	#print("restart\n")
	


	#sp.getoutput("sudo ansible-playbook cron.yml")
	#print("cron")


	
else:
	print(''' <body bgcolor="black"><center><div   class="button button4" style="padding:10px ; font-size:25px ; background-color:black ;margin:36%"><font color="green">Try With Different User Name</font></div></center></body>''')
