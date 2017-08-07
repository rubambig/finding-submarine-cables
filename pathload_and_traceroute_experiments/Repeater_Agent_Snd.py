#!/usr/bin/python3.4

# Sends pathload packets to receiver every 5 minutes
# Sender version
# Code help on timer obtained at https://stackoverflow.com/questions/36952245/subprocess-timeout-failure
# Author Gloire Rubambiza
# Version 07/02/2017

import subprocess
from time import monotonic as mytimer
import time

start = mytimer()

# Wait until 8 hours have gone by
while ( mytimer() - start) <= 288000:
	try:
	    return_code = subprocess.call(["./pathload_snd"])
	except subprocess.TimeoutExpired:
	    print("The child process is done running pathload\n")
     
     # Check the return code before going to sleep
	if return_code != 0:
	    print("Return code error, child process failed")
     
	time.sleep(60*4)


