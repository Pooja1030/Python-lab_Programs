# Program to print the length of the list

    def length(l):
    if not l:
        return 0
    return 1 + length(l[1:])
a = [1, 2, 3, 5, 7, 8]
print("Length of the list is: ")
print(length(a))
