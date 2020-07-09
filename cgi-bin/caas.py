#!/usr/bin/python36
import subprocess as sp
import cgi
import random
print("content-type: text/html")




String = sp.getoutput("netstat -tnlp")
list1=String.split("\n")
list4=[""]

for i in range(1,len(list1)):
        list2=list1[i].split()
        list3=list2[3].split(":")
        list4.extend(list3)







form =cgi.FieldStorage()
name=str(form.getvalue("name"))
image=str(form.getvalue("image"))
port=random.randrange(500,10000,500)

port=str(port)
while port in list4:
	port=str(random.randrange(500,10000,500))


#print(port + name + image)

stra="sudo docker stop " + name 
strb="sudo docker rm " + name 
str1="sudo docker run -dit --name=" + name + " -p "+ port + ":"+ port + " prabhat625/caas:v3"
str3="sudo docker exec -d "+name+" /usr/sbin/sshd -f /etc/ssh/sshd_config"
str2="sudo docker exec -d  "+ name + " /usr/sbin/shellinaboxd -u shellinabox -g shellinabox --cert=/var/lib/shellinabox --port=" + port + " -t -s /:SSH:localhost"
#print(str1)
#print(str2)
sp.getoutput(stra)
sp.getoutput(strb)

sp.getoutput(str1)
sp.getoutput(str3)
sp.getoutput(str2)

loc=str("location: http://192.168.43.228:"+port+"\n")
print(loc)
