#!/usr/bin/python36
import subprocess as sp
import cgi
import random
print("content-type: text/html")


############  port generate   #############

String = sp.getoutput("netstat -tnlp")
list1=String.split("\n")
list4=["6000"]
for i in range(1,len(list1)):
        list2=list1[i].split()
        list3=list2[3].split(":")
        list4.extend(list3)
port=random.randrange(500,10000,500)
port=str(port)
while port in list4:
        port=str(random.randrange(500,10000,500))


############# input  #################


form =cgi.FieldStorage()
name=str(form.getvalue("name"))  
name=name.lower()
image=str(form.getvalue("img"))

############## input-name check ############


docker =sp.getoutput("sudo docker ps -a")

dockerps=docker.split("\n")
list6=[]
for i in range(1,len(dockerps)):
	list5=dockerps[i].split()
	Doc_name=list5[-1]
	list6.append(Doc_name.lower())


#################  Main Logic #############

if name in list6:
	print('\n name already in use')
elif image==str("prabhat625/caas:v3"): 	 
	str1="sudo docker run -dit --name=" + name + " -p "+ port + ":"+ port + " prabhat625/caas:v3"
	str3="sudo docker exec -d "+name+" /usr/sbin/sshd -f /etc/ssh/sshd_config"
	str2="sudo docker exec -d  "+ name + " /usr/sbin/shellinaboxd -u shellinabox -g shellinabox --cert=/var/lib/shellinabox --port=" + port + " -t -s /:SSH:localhost"
	sp.getoutput(str1)
	sp.getoutput(str3)
	sp.getoutput(str2)	
elif image==str("prabhat625/ubuntucaas:v1"):
	str1="sudo docker run -dit --name=" + name + " -p "+ port +  ":8888 prabhat625/ubuntucaas:v1"
	str2="sudo docker exec -d  "+ name + " sudo invoke-rc.d shellinabox start"
	sp.getoutput(str1)
	sp.getoutput(str2)


loc=str("location: http://192.168.43.228/cgi-bin/docker.py\n")	
print(loc)
