# importing 're' to use Regular expression
import re



str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:                      
	print 'found', match.group() ## 'found word:cat'
else:
	print 'did not find'


# searches to see if word 'Bat' is found
whatever = 'I am Batman, king of Gotham!'
match = re.search(r'Bat', whatever)
if match:
	print 'found', match.group()
else:
	print 'did not find'


# finds the three letters after 'Bat'
whatever = 'I am Batman, king of Gotham!'
match = re.search(r'Bat\w\w\w', whatever)
if match:
	print 'found', match.group()
else:
	print 'did not find'


# finds the email
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
	print match.group()  ## 'alice-b@google.com'