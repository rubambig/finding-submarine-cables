#!/usr/bin/python3.4

# Saves given parameters to a CSV File
# Author Gloire Rubambiza
# Version 07/12/2017

import sys

day = str(sys.argv[1])
print("The day is %s" % day)
time = str(sys.argv[2])
print("The day is %s" % time)
sender = str(sys.argv[3])
receiver = str(sys.argv[4])
ip = str(sys.argv[5])
print("The ip address is %s" % ip)
duration = int(float(sys.argv[6]))
print("The duration is %s" % duration)
hop = int(sys.argv[7])
s_file = str(sys.argv[8])

def save_params(day, time, sender, receiver, ip, duration, hop, file_name):
    
    ip = (''.join( c for c in ip if  c not in '()' )).split('.')
    ip_short = ip[0]+"."+ip[1]
    with open(file_name, "a") as FILE:
        line = day+","+time+","+sender+","+receiver+","+ip_short+","+str(duration)+","+str(hop)
        FILE.write(line+"\n")


if __name__ == '__main__':

   save_params(day, time, sender, receiver, ip, duration, hop, s_file)
