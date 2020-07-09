import subprocess as sp

fp=open("vncuser.yml","r")
ch=fp.read()
fp.close()
String ="- hosts: "+user+"\n"
fp1=open("everyvnc.yml","w")
fp1.write(String)
fp1.write(ch)
fp1.close();
print(ch)

