def insertionsSort(Array_):
	for j in range(1, len(Array_)):
		#j starts from index 1(second element) to the end of the array.
		key = Array_[j]
		#set the key to be the element at index 1
		i = j - 1
		#i = 0 at first instance of execution
		while i >= 0 and Array_[i] > key:
			#if i is > or = 0 and the element at index 0 is greater than key is true
			Array_[i+1] = Array_[i]
			#make the element at index 1 be the element at index 0 since its greater
			i = i - 1
			#decrement i
		Array_[i+1] = key
		#whenever the while loops fails, use i from line 12. if while loop doesnt run at all, use i from line 6
	return Array_ 


print(insertionsSort([5, 2, 4, 6, 1, 3, 7, 6, 11]))

