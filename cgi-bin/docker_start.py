#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")


form=cgi.FieldStorage()

name = form.getvalue("name")
name=str(name)
image=str(form.getvalue("image"))
##############  getting active patting port #############

str1 ="sudo docker start "+str(name)
x=sp.getoutput(str1)

docker =sp.getoutput("sudo docker ps -a")
dockerps=docker.split("\n")
list6=[]
port=""
for i in range(1,len(dockerps)):
                list5=dockerps[i].split()
                if name in list5:
                        list7=list5[-2].split("->")
                        list8=list7[-1].split("/")
                        port=list8[0]
                        break
if image==str("prabhat625/caas:v3"):
        str3="sudo docker exec -d "+name+" /usr/sbin/sshd -f /etc/ssh/sshd_config"
        str2="sudo docker exec -d  "+ name + " /usr/sbin/shellinaboxd -u shellinabox -g shellinabox --cert=/var/lib/shellinabox --port=" + port + " -t -s /:SSH:localhost"
        sp.getoutput(str3)
        sp.getoutput(str2)
elif image==str("prabhat625/ubuntucaas:v1"):
        str2="sudo docker exec -d  "+ name + " sudo invoke-rc.d shellinabox start"
        sp.getoutput(str2)

print("location: http://192.168.43.228/cgi-bin/docker.py\n")
