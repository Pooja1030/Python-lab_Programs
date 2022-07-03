import cmath
a= int(input('Enter the value of a: '));
b= int(input('Enter the value of b: '));
c= int(input('Enter the value of c: '));
print("Given quadratic equation is ");
print('{0}x**2+{1}x +{2}=0' .format(a,b,c))

#Quadratic discriminant
d=(b**2)-(4*a*c)

#finding solutions of quadratic equations
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

#printing two solutions
print('solution are{0} and {1}'. format(sol1.sol2))