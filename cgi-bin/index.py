#!/usr/bin/python3
import subprocess as sp
print("content-type: text/html\n")
ssh_service_status_cmd="sudo systemctl is-active ssh"
ds_output = sp.getstatusoutput(ssh_service_status_cmd)
ssh_service_status="stopped"
cmd="which ssh"
output = sp.getstatusoutput(cmd)
ssh_Status_Checking="nothing"
if output[0] == 0:
        ssh_Status_Checking="Installed"
else:
        ssh_Status_Checking="Uninstalled"
if ds_output[1] == 'active':
        ssh_service_status="running"
else:
        ssh_service_status="stopped"
print("<marquee><u>Welcome to SSH Manager</u></marquee>")
print("<form action='sshruns.py' method='GET'>")
print("<center>")
print("""
<table border='5'>
<tr>
<td>Check SSH Software Status</td>
<td>{0}</td>
</tr>
<tr>
<td>Install SSH</td>
<td><a href='sshins.py'>Click Here to Install SSH</a></td>
</tr>
<tr>
<td>SSH service status</td>
<td>{1}</td>
</tr>
<tr>
<td>ssh Service Manager</td>
<td><a href='sshruns.py'>click to start ssh</a></td>
</tr>
<tr>
<td>UserName for SSH</td>
<td><input name="username"/></td>
</tr>
<tr>
<td>Submit</td>
<td><input type="submit" /></td>
</tr>

</table>""".format(ssh_Status_Checking,ssh_service_status))

print("</form>")
print("</center>")
print("<h3><center><a href='http://localhost/cgi-bin/index.py'> Click Here for Main Page </a></center></h3>")
