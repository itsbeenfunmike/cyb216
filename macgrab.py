#!/usr/bin/python

import pprint
import requests
import string 
import subprocess

#Create three files
f_arptable = open( 'arptable', 'w+' )
f_maclist = open( 'maclist', 'w+' )
f_maclookup = open( 'maclookup', 'w+' )

#Give write permissions the three files
subprocess.call([ 'chmod','+w','maclist' ])
subprocess.call([ 'chmod','+w','arptable' ])
subprocess.call([ 'chmod','+w','maclookup' ])

#cols = subprocess.Popen(["arp","-a"],stdout=f)

#Run an arp -a command and write the output to the arptable file
subprocess.Popen(['arp','-a'],stdout=f_arptable)

#Pull the company name from the maclookup and save the value
#in the variable devmon
maclookup_url = 'http://macvendors.co/api%s'
req = requests.get( maclookup_url % 'macs' )
req_result = pprint.pprint(req.json())

#Pull the IP and MAC from the arptable file and put them in the
#maclist file along with the value from devmon
for line in open('arptable'):
    if line.startswith('?'):
        ips = line.split()[1]
        macs = line.split()[3]	
        f_maclist.write('\nIP Address: ' + ips + '\nMAC: ' + macs +
        '\nDevice Manufacturer: ' + devmon + '\n' )

subprocess.Popen(['cat','maclist'])

#print("Phase 1 complete")

#with open('maclist') as fp:
#    for line in fp:
#        #line.getline(1)
#        #mac_field = line.split(':')
#        print('line'+"\n")
