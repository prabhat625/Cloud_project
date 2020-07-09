#!/usr/bin/python36

import subprocess as sp


print("content-type: text/html\n")

print("<html>")

print('<body  bgcolor="black">')

#----------------------------------------#
#--------docker launch-------------------#
#-----------------------------------------#



print('<div  bgcolor="white"  width=80% style="margin:10% 10% 10% 10%">')

print('<br><br><h1><font size=10 color="white">  Docker launch :- </font> </h1>')

print('<form action="docker_launch.py"  bgcolor="white">')
print('<font color="white" size="5">')
print('<h9> Enter Your  Container Name:  </h9>')
print('<input name="name" required pattern="[A-Z][a-z]{3,}"/><br><br><br>')
print('<h9> Choose Image: </h9>')
print('<select name="img" style="padding:4px">')

var=sp.getoutput("sudo docker images")


for i in var.split("\n")[1:]:
        j=i.split()
        print('<option style="margin-right:40px" >'+j[0]+':'+j[1]+'</option>')

print("</select required>")

print('<input type= "submit" style="margin-left:35px ; padding:12px"  value="Launch" />')
print('</font>')
print('</form>')


print("</div>")











print('<div  bgcolor="white"  width=80% style="margin:4% 10% 10% 10%">')
print('<br><br><h1><font size="10" color="white">  Docker Status :- </font> </h1>')


#-------------------------------------#
#---table of html for docker status----#
#-------------------------------------# 

print('<table border = 5px width=100% height=50%  bgcolor="white" style="margin:5% 5% 5% 5%">')

print(""" <tr>
		<th> name </th>
		<th> image </th>
		<th> status </th>
                <th> start </th>
		<th> stop </th>
                <th> terminate </th>
                <th> shell </th>
	  </tr>""")

docker =sp.getoutput("sudo docker ps -a")

list=docker.split("\n")

for i in range(1,len(list)):
	list2=list[i].split()
	name=list2[-1]
	image=list2[1]
	if "Up" in list[i]:
		status="Up"
	else:
		status="Exited"
	print(''' <tr>
	           <td> {} </td>
	           <td> {} </td>
                   <td> {} </td>
		   <td><a href="docker_start.py?name={}&image={}">start</a></td>
		   <td><a href="docker_stop.py?name={}">stop</a></td>
		   <td><a href="docker_terminate.py?name={}">terminate</a></td>
		   <td><a href="docker_shell.py?name={}&image={}" target="_blank">shell</a></td>
		</tr>'''.format(name,image,status,name,image,name,name,name,image))

print("</table>")
print("</div>")

print("</body></html>")
