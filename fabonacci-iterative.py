# series 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
num= int(input('enter your number :'))
first_number=0
second_number=1
temp=0

print(first_number)
print(second_number)
for i in range(0,num):
    temp = first_number + second_number
    first_number = second_number
    second_number = temp
    print(temp)
