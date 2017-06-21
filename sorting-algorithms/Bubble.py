def bubble_sort(ary):
	for i in range(0,len(ary)):
		sort = False				
		for j in range(0,len(ary)-1-i):
			if ary[j] > ary[j+1]:
				temp = ary[j+1]
				ary[j+1] = ary[j]
				ary[j] = temp
				sort = True
		if sort == False:
			break	
	return ary

ary = [7,6,5,4]
print ary
print bubble_sort(ary)
