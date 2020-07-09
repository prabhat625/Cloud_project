#importing python modules
import subprocess as sp

#variables
fro="2016pcecedisti036@poornima.org"
to="distijain98@gmail.com"
pas="dinesh@14"
sub="hello"
body="testing"

#opening file in write mode to write variables
fp=open("/root/Desktop/menu/mailvar.yml",mode='w')

#writing varibles in file
fp.write('from: "{}"\n'.format(fro))
fp.write('to: "{}"\n'.format(to))
fp.write('pass: "{}"\n'.format(pas))
fp.write('sub: "{}"\n'.format(sub))
fp.write('body: "{}"\n'.format(body))

#closing file
fp.close()

#running ansible playbook
x=sp.getoutput("ansible-playbook mail.yml")

