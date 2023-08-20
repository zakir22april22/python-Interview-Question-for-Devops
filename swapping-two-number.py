# swap two Number without using temp variable 

num1 = int(input('enter you first number :'))
num2 = int(input('enter your second number :'))

if num1<num2:
    print('Before swapping numner is :', num1,num2)
    num2=num2+num1  #num2: 20+10=30
    num1=num2-num1  #num1: 30-10=20
    num2=num2-num1  #num2: 20-10=10
    print('After swapping number is:',num1,num2)
else:
    print('Before swapping numner is :', num1,num2)
    num1=num1+num2  #num1: 20+10=30
    num2=num1-num2  #num2: 30-20=10
    num1=num1-num2  #num1: 30-10=20
    print('After swapping number is:',num1,num2)

