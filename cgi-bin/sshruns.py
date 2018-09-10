#!/usr/bin/python3

import subprocess as sp
import cgi
print("content-type: text/html\n")

form = cgi.FieldStorage()

uname = form.getvalue("username")
#print(uname)
output = sp.getstatusoutput("echo 'AllowUsers {}' | sudo tee -a /etc/ssh/sshd_config ".format(uname))
output2=sp.getstatusoutput("sudo systemctl restart ssh")


if output[0] == '0' :
     if output2[0] == '0':
        print("Success")
        print("")
else:
        print("Error!!")

print("<h3><center><a href='http://localhost/cgi-bin/index.py'> Click Here for Main Page </a></center></h3>")

