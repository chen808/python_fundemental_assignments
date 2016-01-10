# function ==========================================
def letter_grades(list):
	for num in list:
		if num >= 90:
			print "Score: ", num, " your grade is A"
		elif num >= 80:
			print "Score: ", num, " your grade is B"
		elif num >= 70:
			print "Score: ", num, " your grade is C"
		elif num >= 60:
			print "Score: ", num, " your grade is D"
		else:
			print "Score: ", num, " your grade is F"
	return
# ===================================================

# set count
count = 0


# create empty list
num_list = []


# prompt user (10 times) to enter in score
while count < 10:
	# prompt user and enter their input into variable 'num'
	num = input("Please enter a score: ")
	# append num to num_list[]
	num_list.append(num)
	# increase the count by 1
	count += 1

print ("Scores and Grades") 

# pass list to function to determine grade
letter_grades(num_list)

print ("End of the program, bye!")



