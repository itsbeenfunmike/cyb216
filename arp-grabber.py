#Steps:
#1 Run the ARP -A command to get Macs and IPs and save as a variable
#2 Get the current date and time in the format: YYYY-MM-DD-0000
#3 Save the current date & time to the RIGHTNOW variable
#4 Create a new file named RIGHTNOW-arp.txt
#5 Write the value of the variable to the file

import subprocess
import datetime

#1
output_arp = str(subprocess.check_output(("arp", "-a")))

#2
getnow = datetime.datetime.now() 

#3
usenow = str(getnow.strftime("%Y%m%d-%H%M%S"))

#4
filename = usenow + "-arp"
f = open(filename, "w+")

#5
f.write(output_arp)

