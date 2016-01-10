# Bubble Sort Practice

arr = [5,2,6,8,1,4]

for i in range(len(arr)-1, 0, -1):
	for j in range(i):
		if arr[j] > arr[j+1]:
			temp = arr[j]
			arr[j] = arr[j+1]
			arr[j+1] = temp

print arr 

# 1) Set 'arr' to be list (we will text this list) 
# 2) Go to line 5
# 3) Print 'arr' list
# 4) If left value is greater then right value then swap!

