'''
This tool is for the automation of nmap scanning. This tool utilizes the nmap library for python2.
The advantage to using this tool as compared to using nmap in the command line is that the results
are outputed to a dictionary for easy navagation, as oppposed to outputting to the terminal. While
it is possible to use os.system('nmap 192.168.1.1 -p20-23,25,80,443 -Pn') to get the same output,
the results are not as easy to navigate because the output structure is designed to be more
viewable than navigatable.

'''
# Import nmap module and nmap custom that contains a few functions for converting raw inputs to lists.
import nmap
import nmapcustom
# Create a PortScanner object
nm = nmap.PortScanner() 
# The ip addresses need to be addded individually or as a CIDR block, as strings, and seperated by commas.
ipAddrs = str(raw_input('What ip addresses would you like to scan? Enter ranges with CIDR notation or as individuals, and all seperated by commas: '))
# Define a list of ports. Again, these need to be seperated by commas.
portString = str(raw_input('\nWhat ports would you like to scan? Seperate with commas: '))
# Convert string of ips to a list
ipList = nmapcustom.ips(ipAddrs)
# Iterate through the IP addresses in ipAddrs
for ipAddr in ipList:
	print 'working on ip ' + ipAddr
	scan = nm.scan(ipAddr, arguments = '-sn')
	if scan['nmap']['scanstats']['uphosts'] == '1':
		# Print the current IP address being scanned
		print "**********\n[+] UPHOST FOUND! Results for the following IP address : ", ipAddr, "\n**********"
		# Conduct the first scan and store the results in the variable scan
		# Here, the structure of the command is (ipaddress, ports, arguments = 'x'), such that x is a string of nmap arguments.
		scan = nm.scan(ipAddr, portString, arguments = '-Pn -T5')
		# Convert the port string to a list
		portList = nmapcustom.ports(portString)
		# Iterate through each value in the portList
		for p in portList:
			try:
				# Store the values of the current port in a new dictionary
				# this dictionary output is the sole purpose of using the nmap
				# module in python as opposed to os.system('nmap 192.168.......')
				currentPortDict = scan['scan'][ipAddr]['tcp'][p]
				# Iterate through the keys and values in the dictionary
				# unless the port is closed
				if currentPortDict['state'] == 'closed':
					print 'Port ' + str(p) + ' is closed.\n'
				elif currentPortDict['state'] == 'open':
					print "\nValues for port ", p
					for k, v in currentPortDict.items():
						# Check to see if k is not Null
						if v != '':
							# Print the key and value to the screen 
							print "      ", k.title(), "  : ", v
			except:
				pass

