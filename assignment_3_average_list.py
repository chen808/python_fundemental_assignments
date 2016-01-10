# Create a program that prints the average
# of the values in the list: 
a = [1, 2, 5, 10, 255, 3]

# initialize total_sum
total_sum = 0

for element in a:
	# total up the values and store in total_sum
	total_sum += element
# print out the total_sum / length of array 'a' to get the average
print total_sum / len(a)