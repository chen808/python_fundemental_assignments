
# Create a program that prints all the odd numbers from 1 to 1000.
# Use the for loop and don't use any array to do this exercise. 
for count in range(1,1000):
	if count % 2 != 0:
		print count

print "********************"

# Create another program that prints all the multiples of
# 5 from 5 to 1,000,000. 
for count in range(5,1000):
	if count % 5 == 0:
		print count