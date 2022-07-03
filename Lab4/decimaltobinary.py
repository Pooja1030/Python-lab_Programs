# Program to convert binary to decimal
def decimalToBinary(n):

    if(n > 1):
        decimalToBinary(n//2)
    print(n % 2, end='')


n = int(input("Enter a decimal no: "))
decimalToBinary(n)


