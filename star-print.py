
# left star print with space
num= int(input('enter your number :'))
for i in range(num):
    for j in range(i+1):
        print('*', end=" ")
    print()  

#reverse of left star print with space
num= int(input('enter your number :'))
for i in range(num):
    for j in range(num-i):
        print('*', end=" ")
    print()     

# left star print without space
num = int(input("enter your number :"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end='')
    for j in range(0,i+1):
        print("*",end='')
    print()         



