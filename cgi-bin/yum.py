#importing python modules
import subprocess as sp

#variables
name="prabhat"
desc="yum configuration"
url="file:///dvd"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/yumvars.yml",mode='w')

#writing varibles in file
fp.write('name: "{}"\n'.format(name))
fp.write('desc: "{}"\n'.format(desc))
fp.write('url: "{}"\n'.format(url))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook yum.yml")

