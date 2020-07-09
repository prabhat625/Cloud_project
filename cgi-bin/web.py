#importing python modules
import subprocess as sp

#variables
name="disti.html"
content="hello world"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/webvar.yml",mode='w')

#writing varibles in file
fp.write('content: "{}"\n'.format(content))
fp.write('name: "{}"\n'.format(name))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook web.yml")

