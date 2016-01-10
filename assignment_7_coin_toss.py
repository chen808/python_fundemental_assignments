# Coin Toss Assignment
import math
import random

# initialize variables head_count and tail_count to 0
head_count=0
tail_count=0

# flip coin 5000 times
for flip in range(0, 5000):
	# each flip generates a random number and rounds it (number only between 1 or 0)
	rand = round(random.random())
	# if random number is 0 then it's tail
	if rand == 0:
		# set face to be 'tail'
		face = 'tail'
		# increase tail_count
		tail_count += 1
	# else it's heads
	else:
		# set face to 'head'
		face = 'head'
		# increse head_count
		head_count += 1

	# print out results after each flip
	print "Attempt #"+str(flip)+": Throwing a coin...It's a "+face+"!...Got "+str(head_count)+" head(s) and "+str(tail_count)+" tail(s) so far"

# end program after 5000th flip
print "Ending the program, thanks!"

