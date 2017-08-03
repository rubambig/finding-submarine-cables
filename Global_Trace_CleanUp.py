#!/usr/bin/python3.4

# Saves given parameters to a CSV File
# Author Gloire Rubambiza
# Version 08/01/2017

import sys

day = str(sys.argv[1])
print("The day is %s" % day)
time = str(sys.argv[2])
print("The time is %s" % time)
sender = str(sys.argv[3])
receiver = str(sys.argv[4])
dns = str(sys.argv[5])
ip = str(sys.argv[6])

# Check for blanks in the traceroute
if "Global" in ip:
    dns = "*"
    ip = "*"
    print("The ip address is %s" % ip)
    duration = "*"
    print("The duration is %s" % duration)
    hop = int(sys.argv[8])
else:
    print("The ip address is %s" % ip)
    duration = int(float(sys.argv[7]))
    print("The duration is %s" % duration)
    hop = int(sys.argv[8])
s_file = str(sys.argv[9])

def save_params(day, time, sender, receiver, dns, ip, duration, hop, file_name):
    
    if "*" in ip:
      with open(file_name, "a") as FILE:
        line = day+","+time+","+sender+","+receiver+","+dns+","+ip+","+str(duration)+","+str(hop)
        FILE.write(line+"\n")
    else:    
       ip = (''.join( c for c in ip if  c not in '()' )).split('.')
       ip = ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]
       #ip = (''.join( c for c in ip if  c not in '()' )).split('.')
       #ip_short = ip[0]+"."+ip[1]
       print("The ip is %s \n" % ip)
       with open(file_name, "a") as FILE:
        line = day+","+time+","+sender+","+receiver+","+dns+","+ip+","+str(duration)+","+str(hop)
        FILE.write(line+"\n")


if __name__ == '__main__':

   save_params(day, time, sender, receiver, dns, ip, duration, hop, s_file)
