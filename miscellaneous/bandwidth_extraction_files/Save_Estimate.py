#!/usr/bin/python3.4

# Saves given parameters to a CSV File
# Author Gloire Rubambiza
# Version 07/06/2017

import sys

day = str(sys.argv[1])
print("The day is %s" % day)
time = str(sys.argv[2])
print("The day is %s" % time)
sender = str(sys.argv[3])
receiver = str(sys.argv[4])
provider = str(sys.argv[5])
print("The provider is %s" % provider)
processor = str(sys.argv[6])
print("The processor is %s" % processor)
lower = int(float(sys.argv[7]))
upper = int(float(sys.argv[8]))
s_file = str(sys.argv[9])

def save_params(day, time, sender, receiver, prov, proc, lower, upper, file_name):
    
    with open(file_name, "a") as FILE:
        line = day+","+time+","+sender+","+receiver+","+prov+","+proc+","+str(lower)+","+str(upper)
        FILE.write(line+"\n")


if __name__ == '__main__':

   save_params(day, time, sender, receiver, provider, processor, lower, upper, s_file)
