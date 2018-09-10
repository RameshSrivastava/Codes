#!/usr/bin/python3

import subprocess as sp
print("content-type: text/html\n")
cmd="sudo apt install -y openssh-server"

output = sp.getstatusoutput(cmd)

if output[0] == 0:
        print("Software Installed Successfully")
        #print("location: index.py")
        #print("")
else:

        print("Software Not Installed Successfully")

print("<h3><center><a href='http://localhost/cgi-bin/index.py'> Click Here for Main Page </a></center></h3>")
