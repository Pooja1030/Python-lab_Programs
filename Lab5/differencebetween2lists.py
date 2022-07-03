#Program to find the difference between two lists

li1 = [35,6,62,86,34,3,4,65]
li2 = [86, 4, 65]
li3 = []

for i in li1 + li2:
    if i not in li1 or i not in li2:
        li3.append(i)

print("List 1 is: ", li1)
print("List 2 is: ", li2)
print("Difference is: ", li3)