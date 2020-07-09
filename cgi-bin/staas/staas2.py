#!/usr/bin/python36
import subprocess as sp
print("content-type: text/html\n")

print('''

<body bgcolor="black">
<div style="margin-top:30%">
   <center style="font-size:100"> <font size="1000" color="white"><h1>&#10003</h1><font><center>
</div>
</body>''')

y=sp.getoutput("sudo ansible-playbook setuser.yml")
