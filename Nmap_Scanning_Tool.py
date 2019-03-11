'''
This tool is for the automation of nmap scanning. This tool utilizes the nmap library for python2.
The advantage to using this tool as compared to using nmap in the command line is that the results
are outputed to a dictionary for easy navagation, as oppposed to outputting to the terminal. While
it is possible to use os.system('nmap 192.168.1.1 -p20-23,25,80,443 -Pn') to get the same output,
the results are not as easy to navigate because the output structure is designed to be more
viewable than navigatable.

'''
# Import nmap module
import nmap
# Create a PortScanner object
nm = nmap.PortScanner()
# The ip addresses need to be addded individually as strings and seperated by commas.
ipAddrs = ['192.168.1.1']
# Define a list of ports. Again, these need to be seperated by commas, but don't have to be strings.
portList = [20,21,22,23,25,80,443]
# The purpose here is to have a single listed string of ports that will directly apply to the nmap scan.
# but we still want the portList for enumeration and iteration near the end when listing outputs by port.
portString = ''
for p in portList:
	portString += str(p) + ','
# Define a list of keys to look for
serviceList = ['product','version','name','script']
# Iterate through the IP addresses in ipAddrs
for i in ipAddrs:
	# Print the current IP address being scanned
	print "\n[+] Results for the following IP address : ", i, "\n"
	# Conduct the first scan and store the results in the variable scan
	# Here, the structure of the command is (ipaddress, ports, arguments = '')
	scan = nm.scan(i, portString, arguments = '-Pn')
	# Iterate through each value in the portList
	for p in portList:
		# Store the values of the current port in a new dictionary
		# this dictionary output is the sole purpose of using the nmap
		# module in python as opposed to os.system('nmap 192.168.......')
		currentPortDict = scan['scan'][i]['tcp'][p]
		# Iterate through the keys and values in the dictionary
		# unless the port is closed
		if currentPortDict['state']=='closed':
			print 'Port ' + str(p) + ' is closed.'
		else:
			print "\nValues for port ", p
			for k, v in currentPortDict.items():
				# Check to see if the key is in our serviceList
				for k in serviceList:
					if v != '':
						# Print the key and value to the screen as
						# as long as not null 
						print "      ", k.title(), "  : ", v
