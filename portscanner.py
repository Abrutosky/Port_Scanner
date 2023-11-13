#Alex Brutosky - port scanner

import socket
import subprocess
import sys
from datetime import datetime #Tells you how long it took to execute

#Blank screen
subprocess.call('clear', shell=True)

#Ask for user input
remoteServer = raw_input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Print a banner with information on the port that we'll be scanning
print "_" * 60
print "please wait, scanning remote host now", remoteServerIP
print "_" * 60

#Check the date and time that the scan was started
t1 = datetime.now()

#Specifying ports using the range function
#And error handling

try:
	for port in range (1,5000):
	    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	    result = sock.connect_ex((remoteServerIP, port))
	    if result == 0:
	       print "Port {}:	  Open".format(port)
	    sock.close()

except KeyboardInterrupt:
       print "You pressed Ctrl+C"
       sys.exit()

except socket.gaierror:
       print "Hostname could not be resolved. Exiting"
       sys.exit()

except socket.error:
       print "Couldn't connect to server"
       sys.exit()

#Checking time once more
t2 = datetime.now()

#Calculate the difference in time to know how long it took to scan
total = t2 - t1

#Printing the info on the screen
print 'Scanning completed in: ', total
 
