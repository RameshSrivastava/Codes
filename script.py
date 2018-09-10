#!/usr/bin/python3
import subprocess as sp

uname = input("Enter username whom should be enabled for SSH:")

ssh_service_status_cmd="systemctl is-active ssh"

s_output = sp.getstatusoutput(ssh_service_status_cmd)

ssh_service_status="stopped"

cmd="which ssh"

output = sp.getstatusoutput(cmd)

ssh_service_status_cmd="systemctl is-active ssh"

s_output = sp.getstatusoutput(ssh_service_status_cmd)

ssh_Status_Checking="nothing"

if output[0] == 0:
        ssh_Status_Checking="Installed"
else:
        ssh_Status_Checking="Uninstalled"
        cmd="sudo apt install -y openssh-server"
        output1 = sp.getstatusoutput(cmd)
        if output1[0] == 0:
              print("Software Installed Successfully")
        else:
              print("Software Not Installed Successfully")


if s_output[1] == 'active':
        ssh_service_status="running"
else:
        ssh_service_status="stopped"
        print(uname)
        output3 = sp.getstatusoutput("echo 'AllowUsers {}' | sudo tee -a /etc/ssh/sshd_config ".format(uname))
        soutput=sp.getstatusoutput("sudo systemctl restart sshd")
        print("Task Successful")

