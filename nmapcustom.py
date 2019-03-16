
def ports(numListStr):
	'''
	Takes a traditional nmap string of ports and converts it to a list of integers.
	'''
	numListSplit = numListStr.split(',')
	finalList = []
	for intORrange in numListSplit:
	     if '-' not in intORrange:
	            finalList.append(int(intORrange))
	     else:
	             rangeEnds = intORrange.split('-')
	             for integer in range(int(rangeEnds[0]),(int(rangeEnds[1])+1)):
	                     finalList.append(integer)
	return (finalList)

def ips(ipListStr):
	import iptools
	'''
	Takes a traditional nmap string of ips and converts it to a list of ips. Only takes individuals or CIDR notation.
	'''
	ipListPrimary = ipListStr.split(',')
	ipListSecondary = []
	for ipElt in ipListPrimary:
		if '/' in ipElt:
			ipRange = iptools.IpRangeList(ipElt)
			ipIter = ipRange.__iter__()
			while True:
				try:
					ipListSecondary.append(next(ipIter))
				except:
					break
		else:
			ipListSecondary.append(ipElt)
		return ipListSecondary

	
