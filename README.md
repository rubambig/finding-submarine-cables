# finding-submarine-cables
CMU-Rwanda-CUBoulder collaboration on understanding submarine networks

- We ran traceroute experiments to get a global perspective on packet latencies using Amazon EC2 instances in Japan, Oregon, and
a Lunix machine located at the Carnegie Mellon University Rwanda campus.

- The remote control of the Japan and Oregon instances was at the University of Colorado Boulder. 

- The experiments were conducted for approximately a week. Each of the three instances ran traceroutes to the other locations
provided in the webserverslist.txt file. In other words, Japan ran a traceroute to Rwanda, Oregon, Algeria, e.t.c while 
Rwanda ran traceroute to Japan, Oregon, Congo D.R, Uganda, e.t.c. 

- For each instance and experimental day, there is a summary file on the latencies and hops for that day. 

- THe data is freely available, just be sure to cite the institutions that supported the data collection

- To contribute to the project or use the data, run the usual:

   `$ git clone https://github.com/rubambig/finding-submarine-cables.git`

For more info, please contact **rubambig@mail.gvsu.edu**

