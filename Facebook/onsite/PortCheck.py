import socket

host = '104.131.0.78'
port = 22

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
    s.shutdown(2)
    print "Success connecting to "
    print host + "on port: " + str(port)
except:
    print "Cannot connect to "
    print host + " on port: " + str(port)
