# Stars Assignment Part 1

# function ======================
def draw_stars (x):
	# traverse through array 'x'
	for i in x:
		# print 'x' by value 'i'
		print '*' * i
# ===============================

# Initial list of  numbers
x = [4, 6, 1, 3, 5, 7, 25]

# Send the list 'x' into function 'draw_stars'
draw_stars(x)