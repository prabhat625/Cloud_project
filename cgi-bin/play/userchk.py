import subprocess as sp
import cgi
form=cgi.FieldStorage()
user=str(form.getvalue("User_Name"))
user=input("user")
storage=sp.getoutput("id {}".format(user))
lil=storage.split(" ")
if "no" in lil:
        print("user not exist")
else :
	print("wigfwief")
