'''
This tool is for the automation of nmap scanning. This tool uses a two fold method for reliable host discovery, followed up by performing an 
aggressive scan only if the host is up, as determined by the -sn switch. The traditional -A switch tends to miss hosts that the -sn switch can
identify, but the -Pn switch which assumes all hosts are up, takes exponentially more time that this program. This program solves the issue
of maximizing both time and reliability.
'''
# Import nmap module and nmap custom that contains a few functions for converting raw inputs to lists.
import nmap
import nmapcustom
import os
# Create a PortScanner object
nm = nmap.PortScanner() 
# The ip addresses need to be added individually or as a CIDR block, as strings, and separated by commas.
ipAddrs = str(raw_input('What ip addresses would you like to scan? Enter ranges with CIDR notation or as individuals, and all seperated by commas: '))
# Define a list of ports. Again, these need to be seperated by commas.
portString = str(raw_input('\nWhat ports would you like to scan? Seperate with commas and groups by dashes: '))
# Convert string of ips to a list
ipList = nmapcustom.ips(ipAddrs)
# Iterate through the IP addresses in ipAddrs
for ipAddr in ipList:
	# First, we will check to see if the host is up.
	# Then we will print the ip being scanned to visually track progress.
	print 'working on ip ' + ipAddr
	scan = nm.scan(ipAddr, arguments = '-sn')
	if scan['nmap']['scanstats']['uphosts'] == '1':
		# Print the current IP address being scanned
		print "**********\n[+] UPHOST FOUND! Results for the following IP address : ", ipAddr, "\n**********"
		# Conduct the scan and print the output that would happen if we were to manually enter the command in the terminal.
		print "Now running \'nmap -A -T5 -p " + portString + " "  + ipAddr + "\'" 
		print os.system('nmap -A -T5 ' + '-p' + portString + ' ' +  ipAddr)

