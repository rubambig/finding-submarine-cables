#!/usr/bin/python3.4

# Repeats traceroute for each web server after a sleep time of 5 minutes.
# Author: Gloire Rubambiza
# Version: 07/21/2017

import subprocess
from time import monotonic as mytimer
import sys
import time

# Global variables
web_server = ""
sender = str(sys.argv[1])
print("The sender is %s\n" % sender)

# Get the directory where to send the file for an experiment.
directory = subprocess.check_output("./Dir_Creation", universal_newlines=True)
directory = directory[:26]

# To be used as the template of return codes.
# It is supposed to be 0, i.e. success every time.
return_code = subprocess.call(["ls"])
print("The return code is %s " % return_code)

# Search for the server to traceroute based on file entries.
try:
    with open("../webservers.txt") as ws:
        entries = ws.readlines()
        countries = [x.strip() for x in entries]
        ws.close()
except IOError as fnf:
    print("webservers.txt file was not found\n")
    print("Please make sure the file is in the globaltrace directory\n")


# Create a directory for each country's  traceroute experiments
for c in countries:
    current_server = c.split(',')
    c_name = current_server[0]
    if c_name == sender:
       print("Ignoring current sender in webserver list\n")
    else:
         subprocess.call(["mkdir", c_name])
         subprocess.call(["mv", c_name, directory])

# Start the timer
start = mytimer()

# Repeat the experiment for 8 hours.
# Script still responds to process control signals, i.e CTRL + C, D, etc.
# Alternatively, the subprocess can be killed by removing it from ps list.
while ( mytimer() - start) <= 28800:
    for c in countries:
        current_server = c.split(',')
        c_name = current_server[0]
        web_server = current_server[1]
        if c_name != sender:
           try:
               country_code = ''.join(c_name[:3])
               print("Running traceroute to %s next\n" % c_name)
               filename = subprocess.check_output(["./FileCreation", country_code], universal_newlines=True)
               
               # Take care of single digit dates.
               if len(filename) == 43:
                  filename = filename[:42]
               else:
                  filename = filename[:43]
               print("Destination file is %s\n" % filename)
               
               # Check the return code before going to sleep.
               # If successful, move the file to its right subdirectory.
               t_open = open(filename, "w")
               return_code = subprocess.call(["traceroute", web_server], stdout=t_open)
               if return_code != 0:
                  print("traceroute for %s file failed\n" % filename)
                  print("Please update/check the list of webservers for inconsistencies\n") 
               t_open.close()
       
               destination = directory+"/"+c_name+"/"
               return_code = subprocess.call(["mv", filename, destination])
               print("Traceroute to %s ran succesfully!\n" % country_code)
               print("The file was saved at %s\n" % destination) 
           except subprocess.CalledProcessError as cpe:
               print("Process of file creation failed!\n")
               print("The return code was %d\n", cpe.returncode)
               print("The output is %s\n", str(cpe.ouput))
 
    time.sleep(60*5)
print("Experiments are done!\n\n")
exit(1)


     
     
    

