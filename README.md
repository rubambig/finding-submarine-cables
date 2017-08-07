# finding-submarine-cables

## global_trace_experiments directory
Experimental location: CMU-Rwanda-CUBoulder collaboration

- We ran [*traceroute*](https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/traceroute.html "traceroute description") experiments to get a global perspective on packet latencies of submarine cables.

- The cloud resources were Amazon EC2 instances in Japan, Oregon, and a Lunix machine located at 
the [Carnegie Mellon University Africa](https://www.cmu.edu/africa/ "CMU Rwanda") campus.

- The script running [*traceroute*](https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/traceroute.html "traceroute description") was put to sleep for 5 minutes after each successful experiment for the ideal amount of 
raw data on a given day.

- The remote control of the Japan and Oregon instances was at the [University of Colorado Boulder](http://www.colorado.edu/cs/ "CU Boulder")(CU Boulder).

- The experiments were conducted for approximately a week. Each of the three instances ran traceroutes to 
the other locations provided in the [webservers.txt](./global_trace_experiments/webserver.txt) file. In other words, Japan ran a traceroute to Rwanda, Oregon, Algeria, e.t.c while Rwanda ran traceroute to Japan, Oregon, Congo D.R, Uganda, e.t.c. 

- For each instance and experimental day, there is a summary file on the latencies and hops for that day. 

- The data is freely available, just be sure to cite the institutions that supported the data collection.

## pathload_and_traceroute_experiments directory
Experimental location: Computer Systems Research lab at CU Boulder

- We ran [*Pathload*](https://www.cc.gatech.edu/~dovrolis/bw-est/pathload_tutorial.html#overview "Pathload description and set up") and [*traceroute*](https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/traceroute.html "traceroute description") experiments for packet routing analysis and bandwidth estimation of submarine cables.

- Using AWS and Google Cloud Platorm, virtual instances were set up to link California to Singapore,
Oregon to Japan, and Ohio to London to get a trans-Pacific and trans-Atlantic view of submarine cable performance.

- Like the global experiments, the remote control was at CU Boulder.

- [*Pathload*](https://www.cc.gatech.edu/~dovrolis/bw-est/pathload_tutorial.html#overview "Pathload description and set up") and [*traceroute*](https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/traceroute.html "traceroute description") required the cooperation of a sender and a receiver in order to run. Hence, 
we allowed all ICMP, UDP, and TCP traffic from anywhere in the world on all instances. 

- [*Pathload*](https://www.cc.gatech.edu/~dovrolis/bw-est/pathload_tutorial.html#overview "Pathload description and set up") and [*traceroute*](https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/traceroute.html "traceroute description") were run simultaneously and timestamped for analysis. After each successful
experiment, the sender's process was put to sleep for 4 minutes while the receiver's process was put
to sleep for 5 minutes (to allow the receiver ample time to wake up and get ready for traffic 
from the sender).

- The experiments were repeated continuously for a week (approx. 8 hours each day).

- The raw data was extracted and analyzed with [R](https://www.r-project.org/about.html "What is R")

- The data is freely available, just be sure to cite the institutions that supported the data collection.

## Acknowledgements
Special thanks to these individuals/institutions for supporting/participating in this data collection:
- Dr. Dirk Grunwald - [University of Colorado Boulder](http://www.colorado.edu/cs/ "CU Boulder")
- Dr. Tim Brown - [Carnegie Mellon University Africa](https://www.cmu.edu/africa/ "CMU Rwanda")
- Mukiibi H. Semwogerere - [Carnegie Mellon University Africa](https://www.cmu.edu/africa/ "CMU Rwanda")


## Contributions
- To contribute to the project or use the data, run the usual:

`$ git clone https://github.com/rubambig/finding-submarine-cables.git`

For questions/more info, please email **rubambig@mail.gvsu.edu**

