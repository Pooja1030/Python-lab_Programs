# intersection of two lists

def intersection(list1,list2):
    
    list3 = [value for value in list1 if value in list2]
    return(list3)
   
list1 = [2,3,7,5,3,2]
list2=[4,6,8,9,3,2]
print(intersection(list1,list2))