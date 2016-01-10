# function that takes in two arguments, multiplies
# each number then returns the list

# function to multiply by 5
def mult_by_b (a, b):
	# creating empty list
	x = []
	# iterating through list
	for count in a:
		# append the amount to empty list 'x' after multiplication
		x.append(count*b)
	# return new list
	return x

# list being sent to function
a = [2,4,10,16] 

# function call to mult_by_b, passing in array 'a' and 5(what to be multiplied by)
b = mult_by_b(a, 5) 

# print out b after it's been processed from function
print b
