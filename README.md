Copy the 'script.py' file to any ubuntu machine and run it using the below command, it will ask for username that has to be enabled for ssh.
'python3 script.py'
Also, the user should have sudo permission to run the above command.

OR

CGI-BIN:-
Create a web server (on whom you want to install SSH) and enable CGI for that server.
Now copy the file inside the CGI-BIN to the document root and access the webpage from anywhere.
Give apache sudo power as it will run commands via a web page on the Ubunntu machine.
