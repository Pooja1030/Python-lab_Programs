# Sort tuples by total digits

def count_digits(M):
    for x in M:
        return sum([len(str(x))])
li = [(34,7,3,54), (3,7,5,25), (23,66,85,3), (33,65,43,23)]
print("Original list is:", li)
li.sort(key=count_digits)
print("Sorted list is:", li)
