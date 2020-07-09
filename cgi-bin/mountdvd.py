#importing python modules
import subprocess as sp

#variables
mountpoint="/dvd"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/mountvar.yml",mode='w')

#writing varibles in file
fp.write('mountpoint: "{}"\n'.format(mountpoint))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook mountdvd.yml")

