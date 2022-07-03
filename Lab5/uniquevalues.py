# Python program to get unique values from list

def unique(list1):
	unique_list = []
	for x in list1:
		if x not in unique_list:
			unique_list.append(x)
	for x in unique_list:
		print (x,end=" ")
	

list1 = [15,23,19,15,45,19,15]
print("The unique values from list are: ")
unique(list1)


