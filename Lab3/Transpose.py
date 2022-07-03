# Program to find transpose of a matrix

n = 4
def transpose(A):

	for i in range(n):
		for j in range(i+1, n):
			A[i][j], A[j][i] = A[j][i], A[i][j]


A = [ [1, 3, 5, 9],
	[2, 7, 4, 6],
	[3, 1, 9, 5],
	[8, 7, 3, 2]]

transpose(A)

print("Resultant matrix is")
for i in range(n):
	for j in range(n):
		print(A[i][j], " ", end='')
	print()
	

