#!/usr/bin/python3.4

# Repeats an experiment after a sleep time of 5 minutes
# Receiver version
# Author Gloire Rubambiza
# Version 07/02/2017

import subprocess
from subprocess import TimeoutExpired
import time

# Get the directory where to send the file for an experiment
directory = subprocess.check_output("./Dir_Creation", universal_newlines=True)
print("The day's directory is %s", directory)
directory = directory[:25]
print("The new day's directory is %s", str(directory))

# To be used as the template of return codes
# It is supposed to be 0, i.e. success every time
return_code = subprocess.call(["ls", "-l"])
print("The return code is %s", return_code)


# Repeat the process until the end of daily experiments
# Send the output to the file of the day
while return_code == 0:
	try:
	    filename = subprocess.check_output(["./FileCreation"], universal_newlines=True)
	    filename = filename[:36]
	except CalledProcessError as cpe:
	    print("Process of file creation failed!\n")
	    print("The return code was %d\n", cpe.returncode)
	    print("The output is %s", str(cpe.ouput))

	try:
            # An example of a sender's DNS
	    sender= "ec2-54-193-94-196.us-west-1.compute.amazonaws.com"
	    return_code = subprocess.call(["./pathload_rcv", "-s", sender, "-o", filename])
	except TimeoutExpired:
	    print("The child process is done running pathload\n")
     
     # Check the return code before going to sleep
	# Check the return code before going to sleep
	# If successful, move the file to its right directory
	if return_code != 0:
	    print("Return code error, child process failed")
	else:
	    return_code = subprocess.call(["mv", filename, directory])
	    trace_filename = filename[:33] + "_trace"
	    t_open = open(trace_filename, "w")
	    try:
	       return_code = subprocess.call(["traceroute", sender], stdout=t_open)
	       t_open.close()
	       return_code = subprocess.call(["mv", trace_filename, directory])
	    except TimeoutExpired:
	       print("The traceroute was not successful!\n")
	time.sleep(60*5)
     
     
    

