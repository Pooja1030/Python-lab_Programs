# Program to convert binary to decimal

# Program to convert binary to decimal
def binaryToDecimal(n):
	num = n;
	dec_value = 0;
	
	# Initializing base
	
	base = 1;
	
	temp = num;
	while(temp):
		last_digit = temp % 10;
		temp = int(temp / 10);
		
		dec_value += last_digit * base;
		base = base * 2;
	return dec_value;


num = 10101011;
print(binaryToDecimal(num));


